"""Bottleneck dependency graph — the core stockify model.

Primary thesis: AI makes cognition/design progressively cheaper, so value
migrates into whatever physical resource is hardest to scale next. Bottlenecks
form cascades (GPUs -> HBM -> DRAM -> storage) and can also *collapse* when AI
obsoletes the layer it just pumped (the memory-collapse scenario). Both
dynamics live in one graph:

  node:   a physical resource that can bind (reducers, HBM, metrology...)
  edge:   depends_on (upstream constraint) / relieved_by (tech that dissolves it)
  signal: kill_signals — observables that say the bottleneck is breaking

Scoring is transparent and deterministic:
  conviction = 0.5 * prevalence + 0.3 * (1 - crowdedness) + 0.2 * evidence
  prevalence   0-1  how binding is it right now (orders, lead times, prices)
  crowdedness  0-1  how priced-in (ETF exists? multiples? star ratings?)
  evidence     0-1  normalized count of attached evidence items

Rebalance rule: overweight binding+uncrowded, hold binding+crowded (it is the
indicator), watch emerging, cut on kill-signal trigger. Never edits core
feedify files — graph lives in data/bottlenecks/*.json, prices are passed in.

Stdlib only.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "data" / "bottlenecks" / "graph_v1.json"

STATUS_ORDER = {"binding": 0, "emerging": 1, "latent": 2, "solved": 3}


def load_graph(path: Path = GRAPH_PATH) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def score_node(node: dict) -> float:
    prevalence = float(node.get("prevalence", 0.5))
    crowdedness = float(node.get("crowdedness", 0.5))
    evidence = min(1.0, len(node.get("evidence", [])) / 5.0)
    return round(0.5 * prevalence + 0.3 * (1 - crowdedness) + 0.2 * evidence, 3)


def rank(graph: dict) -> list[tuple[float, dict]]:
    scored = [(score_node(n), n) for n in graph.get("nodes", [])]
    scored.sort(key=lambda t: (STATUS_ORDER.get(t[1].get("status", "latent"), 9), -t[0]))
    return scored


def rebalance_action(node: dict, score: float) -> str:
    status = node.get("status", "latent")
    crowded = float(node.get("crowdedness", 0.5))
    if status == "solved":
        return "EXIT — thesis played out or dissolved"
    if status == "binding" and crowded < 0.5 and score >= 0.55:
        return "OVERWEIGHT — binding and not yet crowded"
    if status == "binding":
        return "HOLD — owns the bottleneck; doubles as regime indicator"
    if status == "emerging" and score >= 0.5:
        return "ACCUMULATE — n+1 candidate, scale on confirmation"
    if status == "emerging":
        return "WATCH — track kill/confirm signals"
    return "IGNORE — latent"


def check_kill_signals(node: dict, triggered: list[str] | None = None) -> list[str]:
    """Return kill signals worth watching. `triggered` marks confirmed ones.

    Kill signals are manual observations for now (spot prices, order cuts,
    architecture papers). A triggered signal downgrades the node on render.
    """
    triggered = set(triggered or [])
    out = []
    for sig in node.get("kill_signals", []):
        flag = " [TRIGGERED]" if sig in triggered else ""
        out.append(f"{sig}{flag}")
    return out


def short_score(node: dict, triggered: list[str] | None = None) -> float:
    """The digger trade: short crowded picks-and-shovels at dissolution.

    A short only exists where a crowded long exists — binding nodes with
    high crowdedness. Score rises as kill signals trigger:
      short = crowdedness * (0.3 + 0.7 * triggered_ratio)
    Emerging nodes score nothing here: shorting hope is not this trade.
    """
    if node.get("status") != "binding":
        return 0.0
    kills = node.get("kill_signals", [])
    trig = set(triggered or [])
    ratio = (sum(1 for k in kills if k in trig) / len(kills)) if kills else 0.0
    return round(float(node.get("crowdedness", 0.5)) * (0.3 + 0.7 * ratio), 3)


def short_action(node: dict, sscore: float, triggered: list[str] | None = None) -> str:
    if node.get("status") != "binding":
        return ""
    if triggered:
        return "SHORT WATCH — crowded long + kill confirmed; define risk (puts/spreads), pair vs the dissolver"
    if sscore >= 0.2:
        return "DISSOLUTION WATCH — crowded; size any short only on kill trigger"
    return ""


def dissolution_board(graph: dict, moves: dict | None = None,
                      triggered: dict[str, list[str]] | None = None) -> str:
    """Rank binding nodes by short_score: where the digger kills the shovel."""
    moves = moves or {}
    triggered = triggered or {}
    rows = []
    for node in graph.get("nodes", []):
        if node.get("status") != "binding":
            continue
        trig = triggered.get(node["id"], [])
        rows.append((short_score(node, trig), node, trig))
    rows.sort(key=lambda t: -t[0])
    lines = ["# Dissolution board — short the shovels when the digger arrives"]
    for sscore, node, trig in rows:
        tickers = node.get("tickers", [])
        priced = " ".join(
            f"{t}{moves[t]['pct_1d']:+.1f}%" for t in tickers if t in moves
        ) or "unpriced"
        action = short_action(node, sscore, trig)
        flag = "  !! TRIGGERED" if trig else ""
        lines.append(f"## {node['label']} (short {sscore:.2f}){flag}")
        lines.append(f"   crowded long: {' '.join(tickers) or '-'} | 1d: {priced}")
        lines.append(f"   digger (the relief): {', '.join(node.get('relieved_by', [])) or '?'}")
        if node.get("precedents"):
            lines.append(f"   rhymes with: {', '.join(node['precedents'])} (see precedents.json)")
        if action:
            lines.append(f"   -> {action}")
        lines.append("")
    return "\n".join(lines)


def render(graph: dict, moves: dict | None = None,
           triggered: dict[str, list[str]] | None = None) -> str:
    """Full text brief: ranked bottlenecks with live prices + rebalance."""
    moves = moves or {}
    triggered = triggered or {}
    lines = [f"# Bottleneck status — {graph.get('name', 'graph')}"]
    lines.append(f"Thesis: {graph.get('thesis', '')}\n")
    for score, node in rank(graph):
        tickers = node.get("tickers", [])
        priced = " ".join(
            f"{t}{moves[t]['pct_1d']:+.1f}%" for t in tickers if t in moves
        ) or "unpriced"
        action = rebalance_action(node, score)
        trig = triggered.get(node["id"], [])
        warn = "  !! KILL SIGNAL TRIGGERED" if trig else ""
        lines.append(f"## [{node['status'].upper()}] {node['label']} (conviction {score:.2f}){warn}")
        lines.append(f"   tickers: {' '.join(tickers) or '-'} | 1d: {priced}")
        lines.append(f"   -> {action}")
        if node.get("relieved_by"):
            lines.append(f"   dissolved by: {', '.join(node['relieved_by'])}")
        for sig in check_kill_signals(node, trig):
            lines.append(f"   kill-watch: {sig}")
        lines.append("")
    lines.append(dissolution_board(graph, moves, triggered))
    return "\n".join(lines)
