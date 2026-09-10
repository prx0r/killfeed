"""Dissolution recognition model — quantitative gates for both sides.

Primary thesis (user): AI invents new ways of doing things, so bottlenecks
migrate AND dissolve faster than before. Every physical layer — including
energy — can be dissolved by the next method. This module turns that into
numbers: when is a bottleneck binding (own it), crowded (stop adding), and
dissolving (short the shovels).

All thresholds calibrated from data/bottlenecks/precedents.json:
  crowded equity unwinds 70-99% | commodity legs 80-95% | 1-4yr peak->trough.

RECOGNITION GATES (binding — is there a bottleneck?):
  spot_vs_peak >= 0.85          still binding (first crack below)
  price_runup_2yr >= 3.0        parabolic = crowded, not undiscovered
  book_to_bill >= 1.2           orders outrun shipments (ALNT 1.31)
  lead_time_x >= 2.0            lead times 2x normal
  thematic_vehicle + top3 > 0.6 ETF exists, concentrated = priced-in

DISSOLUTION GATES (is the digger arriving?):
  spot_vs_peak < 0.85           first kill (-15% from peak)
  spot_vs_peak < 0.70           confirmed break
  supply_response > 1.5         announced capacity vs demand growth (solar 10x)
  inventory_build = true        double-ordering confessions (DRAM 2019)
  substitution_milestone = true benchmarks/design wins (Z1 benches, Linux moment)
  kill_ratio >= 0.5             half the graph's kill signals confirmed

Missing readings score neutral (0.5) with renormalized weights — the graph's
prevalence/crowdedness priors carry sparse nodes. Scores improve as the
kill-feed accumulates; that accumulation IS the compounding asset.

Stdlib only. Pure functions: graph + precedents + readings in, scores out.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH_PATH = ROOT / "data" / "bottlenecks" / "graph_v1.json"
PRECEDENTS_PATH = ROOT / "data" / "bottlenecks" / "precedents.json"
READINGS_GLOB = "data/bottlenecks/readings_*.json"


def load_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def base_rates(precedents: dict | None = None) -> dict:
    """Median unwind magnitudes parsed from the precedent set.

    Returns median peak-to-trough % for equity legs and commodity legs.
    Recompute as the precedent set grows — this is the EV anchor.
    """
    precedents = precedents or load_json(PRECEDENTS_PATH, {"precedents": []})
    eq, com = [], []
    for p in precedents.get("precedents", []):
        nums = [float(x) for x in re.findall(r"~?-(\d+(?:\.\d+)?)%", p.get("drawdown", ""))]
        if not nums:
            continue
        worst = max(nums)
        # commodity legs mention /kg or carbonate or spot; else equity
        if re.search(r"/kg|carbonate|spot|NAND", p.get("drawdown", ""), re.I):
            com.append(worst)
        eq.append(worst)
    def med(xs):
        xs = sorted(xs)
        return round(xs[len(xs) // 2], 1) if xs else 0.0
    return {
        "median_equity_unwind_pct": med(eq),
        "median_commodity_unwind_pct": med(com),
        "n": len(precedents.get("precedents", [])),
    }


def _wmean(pairs: list[tuple[float | None, float]]) -> float:
    num = sum(v * w for v, w in pairs if v is not None)
    den = sum(w for v, w in pairs if v is not None)
    return num / den if den else 0.5


def binding_score(node: dict, reading: dict | None = None) -> dict:
    """0-1: how binding is this bottleneck right now."""
    r = reading or {}
    spot = r.get("spot_vs_peak")
    runup = r.get("price_runup_2yr")
    btb = r.get("book_to_bill")
    lead = r.get("lead_time_x")
    # A thematic vehicle confirms the bottleneck is real; its absence is
    # neutral (undiscovered), never negative — crowdedness carries pricing.
    vehicle = 0.7 if r.get("thematic_vehicle") else None
    comps = [
        (min(1.0, spot / 0.85) if spot is not None else None, 0.3),
        (min(1.0, runup / 3.0) if runup is not None else None, 0.2),
        (min(1.0, btb / 1.2) if btb is not None else None, 0.2),
        (min(1.0, lead / 2.0) if lead is not None else None, 0.15),
        (vehicle, 0.15),
    ]
    read_score = _wmean(comps)
    prior = float(node.get("prevalence", 0.5))
    combined = round(0.6 * prior + 0.4 * read_score, 3)
    return {"binding": combined, "from_readings": round(read_score, 3), "prior": prior}


def dissolution_score(node: dict, reading: dict | None = None,
                      triggered: list[str] | None = None) -> dict:
    """0-1: how far along is the dissolution."""
    r = reading or {}
    trig = set(triggered or [])
    kills = node.get("kill_signals", [])
    kill_ratio = (sum(1 for k in kills if k in trig) / len(kills)) if kills else 0.0
    spot = r.get("spot_vs_peak")
    spot_break = max(0.0, min(1.0, (0.85 - spot) / 0.35)) if spot is not None else None
    supply = r.get("supply_response")
    glut = min(1.0, max(0.0, (supply - 1.0) / 1.0)) if supply is not None else None
    sub = 1.0 if r.get("substitution_milestone") else (0.0 if "substitution_milestone" in r else None)
    inv = 1.0 if r.get("inventory_build") else (0.0 if "inventory_build" in r else None)
    comps = [(kill_ratio, 0.35), (spot_break, 0.25), (glut, 0.2), (sub, 0.1), (inv, 0.1)]
    return {
        "dissolution": round(_wmean(comps) if any(v is not None for v, _ in comps) else kill_ratio, 3),
        "kill_ratio": round(kill_ratio, 3),
    }


def regime(node: dict, reading: dict | None = None,
           triggered: list[str] | None = None) -> dict:
    """One-word regime + both scores. Calibrated to reproduce the board."""
    b = binding_score(node, reading)["binding"]
    d = dissolution_score(node, reading, triggered)["dissolution"]
    crowded = float(node.get("crowdedness", 0.5))
    status = node.get("status", "latent")
    if status == "solved" or d >= 0.6:
        reg = "EXIT"
    elif status == "binding" and (d >= 0.4 or (triggered and d >= 0.25)):
        reg = "SHORT_WATCH"
    elif status == "binding" and (d >= 0.2 or crowded >= 0.7):
        reg = "DISSOLUTION_WATCH"
    elif status == "binding" and crowded < 0.5 and b >= 0.55:
        reg = "OVERWEIGHT"
    elif status == "binding":
        reg = "HOLD"
    elif status == "emerging" and b >= 0.5 and crowded < 0.5:
        reg = "ACCUMULATE"
    elif status == "emerging":
        reg = "WATCH"
    else:
        reg = "IGNORE"
    return {"regime": reg, "binding": b, "dissolution": d,
            "crowdedness": crowded, "status": status}


def score_all(graph: dict, readings: dict[str, dict] | None = None,
              triggered: dict[str, list[str]] | None = None) -> list[dict]:
    """Score every node; readings keyed by node id."""
    readings, triggered = readings or {}, triggered or {}
    out = []
    for node in graph.get("nodes", []):
        r = regime(node, readings.get(node["id"]), triggered.get(node["id"], []))
        out.append({"id": node["id"], "label": node["label"], **r,
                    "tickers": node.get("tickers", [])})
    order = {"EXIT": 0, "SHORT_WATCH": 1, "DISSOLUTION_WATCH": 2, "OVERWEIGHT": 3,
             "HOLD": 4, "ACCUMULATE": 5, "WATCH": 6, "IGNORE": 7}
    out.sort(key=lambda x: (order.get(x["regime"], 9), -x["binding"]))
    return out


def load_readings(root: Path = ROOT) -> dict[str, dict]:
    """Merge all readings_*.json files, latest date wins per node."""
    merged: dict[str, dict] = {}
    for path in sorted(root.glob(READINGS_GLOB)):
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        for entry in doc.get("readings", []):
            nid = entry.get("node_id")
            if not nid:
                continue
            prev = merged.get(nid, {})
            if entry.get("date", "") >= prev.get("date", ""):
                merged[nid] = entry
    return merged
