#!/usr/bin/env python3
import json, sys, requests
keyword = " ".join(sys.argv[1:]) or "artificial intelligence"
payload={"subawards":False,"limit":20,"page":1,"filters":{"keywords":[keyword],"time_period":[{"start_date":"2025-01-01","end_date":"2026-12-31"}]}}
r=requests.post("https://api.usaspending.gov/api/v2/search/spending_by_award/",json=payload,timeout=30)
r.raise_for_status(); print(json.dumps(r.json(), ensure_ascii=False))
