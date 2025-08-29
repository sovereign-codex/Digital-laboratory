#!/usr/bin/env python3
import argparse, json, os, hashlib
from datetime import date

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", required=True, help="Path to Daily_Laboratory_Scroll_YYYY-MM-DD.pdf")
    ap.add_argument("--manifest", default="data/manifest.json")
    args = ap.parse_args()

    if not os.path.exists(args.pdf):
        raise SystemExit(f"PDF not found: {args.pdf}")

    fname = os.path.basename(args.pdf)
    if not fname.startswith("Daily_Laboratory_Scroll_") or not fname.endswith(".pdf"):
        raise SystemExit("Filename must be Daily_Laboratory_Scroll_YYYY-MM-DD.pdf")

    with open(args.manifest, "r", encoding="utf-8") as f:
        m = json.load(f)

    checksum = sha256_file(args.pdf)
    date_str = fname.replace("Daily_Laboratory_Scroll_", "").replace(".pdf", "")

    # upsert entry
    found = False
    for e in m.get("entries", []):
        if e.get("date") == date_str:
            e["file"] = f"data/scrolls/{fname}"
            e["checksum"] = checksum
            found = True
            break
    if not found:
        m.setdefault("entries", []).append({
            "date": date_str,
            "title": f"Daily Laboratory Scroll — {date_str}",
            "file": f"data/scrolls/{fname}",
            "checksum": checksum
        })

    m["entries"] = sorted(m["entries"], key=lambda e: e["date"], reverse=True)
    m["updated"] = date.today().isoformat()

    with open(args.manifest, "w", encoding="utf-8") as f:
        json.dump(m, f, indent=2)

    print(f"Manifest updated with {fname} ({checksum[:12]}...).")

if __name__ == "__main__":
    main()
