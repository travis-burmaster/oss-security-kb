import json, urllib.request
candidates = [
    ("npm", "express"),
    ("crates.io", "serde"),
    ("OSS-Fuzz", "openssl"),
]
for eco, name in candidates:
    req = urllib.request.Request(
        'https://api.osv.dev/v1/query',
        data=json.dumps({"package": {"ecosystem": eco, "name": name}}).encode(),
        headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
    except Exception as e:
        data = {"error": str(e)}
    print(f'## {eco}/{name}')
    print(json.dumps(data, indent=2)[:30000])
    print()
