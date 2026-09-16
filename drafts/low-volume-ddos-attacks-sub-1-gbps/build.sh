#!/bin/sh
# Reproducible build for this draft: md -> html (+ schema graph) -> screenshots + pdf
set -e
cd "$(dirname "$0")"
R=../../scripts
SLUG=low-volume-ddos-attacks-sub-1-gbps
python3 $R/blog_render.py --md $SLUG.md --out-dir . --hero hero.png --pdf-engine none >/dev/null
mv -f "$(ls -t *.html | head -1)" $SLUG.html
python3 inject_schema.py
python3 render_assets.py
