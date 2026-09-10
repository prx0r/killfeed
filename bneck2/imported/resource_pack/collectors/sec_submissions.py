#!/usr/bin/env python3
import json, os, sys, requests
cik = str(int(sys.argv[1])).zfill(10)
ua = os.getenv("SEC_USER_AGENT","AGI-bottleneck-research contact@example.com")
r = requests.get(f"https://data.sec.gov/submissions/CIK{cik}.json", headers={"User-Agent":ua,"Accept-Encoding":"gzip, deflate"}, timeout=20)
r.raise_for_status(); print(json.dumps(r.json(), ensure_ascii=False))
