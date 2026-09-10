#!/usr/bin/env python3
import json, sys, requests
q = " ".join(sys.argv[1:]) or "AI"
r = requests.get("https://gamma-api.polymarket.com/markets", params={"q":q,"active":"true","closed":"false","limit":50}, timeout=20)
r.raise_for_status()
for m in r.json():
    print(json.dumps({"source_type":"prediction_market","platform":"polymarket","id":m.get("slug") or m.get("conditionId"),"question":m.get("question"),"outcomePrices":m.get("outcomePrices"),"volume":m.get("volume"),"liquidity":m.get("liquidity")}, ensure_ascii=False))
