"""bneck2 lab — cg-flow experimentation loop (see third_party/cg SPEC/AGENTS).

Flow (formalized from cogymkernel, adapted to evidence work):
  HYPOTHESIZE -> PREREGISTER -> RUN -> RECEIPT -> VERDICT -> NEXT

Rules borrowed verbatim in spirit:
- Receipts (JSONL) are canonical. Projections (reports) rebuild from them;
  deleting a projection destroys no evidence (cg §56 idea).
- Gates dominate objectives: a hypothesis needs a FALSIFIER up front, or
  it is not a hypothesis — it's a vibe. Vibes go in notes/, never verdicts.
- PILOT honesty: n<30 decisions => directional only, labelled everywhere.
- Determinism: receipts carry input hashes; same inputs => same verdict.
- LLM judgment never enters a verdict. It may propose hypotheses; only
  measured data disposes them.
"""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "experimentation"
HYPS = LAB / "hypotheses"
RECEIPTS = LAB / "receipts.jsonl"

VERDICTS = ("CONFIRMED", "REFUTED", "INCONCLUSIVE")


def utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def preregister(hyp_id: str, title: str, prediction: str, falsifier: str,
                data: str = "", status: str = "open") -> Path:
    """Write the hypothesis file if absent; never overwrite (append-only)."""
    HYPS.mkdir(parents=True, exist_ok=True)
    path = HYPS / f"{hyp_id}.md"
    if not path.exists():
        path.write_text(
            f"# {hyp_id}: {title}\n\n"
            f"- status: {status}\n"
            f"- prediction: {prediction}\n"
            f"- falsifier: {falsifier}\n"
            f"- data: {data}\n",
            encoding="utf-8")
    return path


def receipt(hyp_id: str, result: dict, verdict: str, n: int,
            ts: str = "") -> dict:
    assert verdict in VERDICTS, f"verdict must be one of {VERDICTS}"
    blob = json.dumps(result, sort_keys=True, default=str)
    row = {"ts": ts or utcnow(), "hyp": hyp_id,
           "inputs_hash": hashlib.sha256(blob.encode()).hexdigest()[:16],
           "n": n, "verdict": verdict,
           "directional_only": n < 30,
           "result": result}
    LAB.mkdir(parents=True, exist_ok=True)
    with open(RECEIPTS, "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    return row


def load_receipts(hyp_id: str = "") -> list[dict]:
    try:
        rows = [json.loads(l) for l in RECEIPTS.read_text(encoding="utf-8").splitlines()
                if l.strip()]
    except (OSError, ValueError):
        return []
    return [r for r in rows if not hyp_id or r.get("hyp") == hyp_id]


def report() -> str:
    """Projection rebuilt purely from receipts (delete-safe)."""
    rows = load_receipts()
    by: dict[str, list[dict]] = {}
    for r in rows:
        by.setdefault(r.get("hyp", "?"), []).append(r)
    lines = ["# Experiment report — rebuilt from receipts",
             f"receipts={len(rows)} hypotheses={len(by)}"]
    for hyp, rs in sorted(by.items()):
        last = rs[-1]
        flag = " (directional-only)" if last.get("directional_only") else ""
        lines.append(f"\n## {hyp}: {last['verdict']}{flag} "
                     f"(n={last.get('n')}, runs={len(rs)})")
        res = last.get("result", {})
        note = res.get("note") or res.get("summary") or ""
        if note:
            lines.append(f"   {str(note)[:300]}")
    return "\n".join(lines)
