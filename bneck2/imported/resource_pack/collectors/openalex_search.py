#!/usr/bin/env python3
import json, sys, requests
q = " ".join(sys.argv[1:]) or "memory bandwidth AI"
r = requests.get("https://api.openalex.org/works", params={"search":q,"sort":"publication_date:desc","per-page":25}, timeout=20)
r.raise_for_status()
for x in r.json().get("results",[]):
    print(json.dumps({"source_type":"paper","id":x.get("id"),"title":x.get("title"),"publication_date":x.get("publication_date"),"cited_by_count":x.get("cited_by_count"),"doi":x.get("doi")}, ensure_ascii=False))
