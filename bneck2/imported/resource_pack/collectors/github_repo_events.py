#!/usr/bin/env python3
import json, os, sys, requests
owner, repo = sys.argv[1], sys.argv[2]
token = sys.argv[3] if len(sys.argv)>3 else os.getenv("GITHUB_TOKEN")
headers={"Accept":"application/vnd.github+json","User-Agent":"agi-bottleneck-radar"}
if token: headers["Authorization"]=f"Bearer {token}"
for endpoint in ["commits","releases","branches"]:
    r=requests.get(f"https://api.github.com/repos/{owner}/{repo}/{endpoint}",headers=headers,params={"per_page":30},timeout=20)
    if r.ok: print(json.dumps({"source_type":"github","owner":owner,"repo":repo,"endpoint":endpoint,"items":r.json()},ensure_ascii=False))
