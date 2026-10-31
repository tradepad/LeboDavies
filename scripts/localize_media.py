#!/usr/bin/env python3
"""Download every image and video the site loads from Wix and point the pages at the local copies.

Run from the repository root:  python3 scripts/localize_media.py

Do this before closing the Wix account, so the site keeps working without Wix.
"""
import hashlib
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
MEDIA = ROOT / "assets" / "media"
PAGES = [ROOT / "index.html", *sorted((ROOT / "news").glob("*.html"))]
URL_RE = re.compile(r"https://(?:static|video)\.wixstatic\.com/[^\s\"')]+")


def local_name(url):
    # Video URLs end in /file, so the extension comes from the host
    if "video.wixstatic.com" in url:
        ext = ".mp4"
    else:
        ext = pathlib.PurePosixPath(url).suffix or ".jpg"
    return hashlib.sha1(url.encode()).hexdigest()[:16] + ext


def main():
    MEDIA.mkdir(parents=True, exist_ok=True)
    urls = sorted({u for page in PAGES for u in URL_RE.findall(page.read_text())})
    mapping = {}

    for url in urls:
        target = MEDIA / local_name(url)
        if not target.exists():
            print("downloading", url)
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                target.write_bytes(resp.read())
        mapping[url] = target

    for page in PAGES:
        text = page.read_text()
        for url, target in mapping.items():
            rel = pathlib.Path(*[".."] * (len(page.relative_to(ROOT).parts) - 1), target.relative_to(ROOT))
            text = text.replace(url, rel.as_posix())
        page.write_text(text)

    print(f"done: {len(mapping)} files in {MEDIA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
