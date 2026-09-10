"""bneck2 lab tests — preregister/receipt/report honesty properties."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from bneck2 import lab as LAB


class TestLab(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = Path(tempfile.mkdtemp())
        self._r, self._h = LAB.RECEIPTS, LAB.HYPS
        LAB.RECEIPTS = self.tmp / "receipts.jsonl"
        LAB.HYPS = self.tmp / "hypotheses"

    def tearDown(self):
        LAB.RECEIPTS, LAB.HYPS = self._r, self._h
        import shutil
        shutil.rmtree(self.tmp, ignore_errors=True)
    def test_pilot_flag(self):
        r = LAB.receipt("TEST-H", {"x": 1}, "CONFIRMED", 3,
                        ts="2026-09-10T00:00:00Z")
        self.assertTrue(r["directional_only"])
        self.assertEqual(len(r["inputs_hash"]), 16)

    def test_no_pilot_flag_at_30(self):
        r = LAB.receipt("TEST-H", {"x": 1}, "REFUTED", 30,
                        ts="2026-09-10T00:00:00Z")
        self.assertFalse(r["directional_only"])

    def test_bad_verdict_rejected(self):
        with self.assertRaises(AssertionError):
            LAB.receipt("TEST-H", {}, "MAYBE", 5)

    def test_report_rebuilds(self):
        LAB.receipt("TEST-H", {"x": 1}, "CONFIRMED", 3,
                    ts="2026-09-10T00:00:00Z")
        rep = LAB.report()
        self.assertIn("TEST-H", rep)


if __name__ == "__main__":
    unittest.main()
