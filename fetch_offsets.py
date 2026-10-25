import argparse, json, os, sys, urllib.request

API = "https://rbxoffsets.com/api/v1/windows/offsets"
BASE = os.path.dirname(os.path.abspath(__file__))

def fetch(version=None, tier="verified"):
    if version is None:
        url = f"{API}/latest"
        meta = json.loads(urllib.request.urlopen(url).read())
        version = meta["version"] if isinstance(meta, dict) and "version" in meta else meta.get("build", "latest")
        # resolve version string
        try:
            version = meta["version"]
        except Exception:
            pass
    print("Target version:", version)
    outdir = os.path.join(BASE, "offsets", version)
    os.makedirs(outdir, exist_ok=True)
    for ext in ("hpp", "json", "txt"):
        q = f"?tier={tier}" if tier else ""
        url = f"{API}/{version}/{ext}{q}"
        try:
            data = urllib.request.urlopen(url).read()
            with open(os.path.join(outdir, f"offsets.{ext}"), "wb") as f:
                f.write(data)
            print("  saved", ext, len(data), "bytes")
        except Exception as e:
            print("  skip", ext, e)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=None)
    ap.add_argument("--tier", default="verified")
    args = ap.parse_args()
    fetch(args.version, args.tier)

if __name__ == "__main__":
    main()
