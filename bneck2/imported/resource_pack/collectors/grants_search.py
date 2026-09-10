#!/usr/bin/env python3
import json, sys, requests
keyword=" ".join(sys.argv[1:]) or "quantum computing"
payload={"keyword":keyword,"oppStatuses":"posted|forecasted","rows":25,"startRecordNum":0}
r=requests.post("https://api.grants.gov/v1/api/search2",json=payload,timeout=30)
r.raise_for_status(); print(json.dumps(r.json(), ensure_ascii=False))
