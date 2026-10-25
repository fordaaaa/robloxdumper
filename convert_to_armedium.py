import argparse, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))

def convert(version):
    src = os.path.join(BASE, "offsets", version, "offsets.hpp")
    if not os.path.exists(src):
        print("missing", src); sys.exit(1)
    with open(src, encoding="utf-8", errors="ignore") as f:
        text = f.read()
    # The rbxoffsets hpp is already in `namespace Offsets { namespace X { ... } }` form.
    # Just copy it as-is into converted/<version>/offsets.h with a version header.
    outdir = os.path.join(BASE, "converted", version)
    os.makedirs(outdir, exist_ok=True)
    outpath = os.path.join(outdir, "offsets.h")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(f"// Auto-generated from rbxoffsets.com for {version}\n")
        f.write(text)
    print("wrote", outpath)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", required=True)
    args = ap.parse_args()
    convert(args.version)

if __name__ == "__main__":
    main()
