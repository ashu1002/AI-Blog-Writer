# Draft: Sub-1 Gbps Attacks (nexusguard.com)

Built from `outlines/sub-1-gbps-ddos-attacks-outline.md`.

## Rebuild

    sh build.sh

`build.sh` runs `blog_render.py` (md to html), then `inject_schema.py`, then
`render_assets.py`. Requires `python-markdown`, `pillow` and `patchright`,
with Chromium at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.

## Why two extra build steps

`blog_render.py` emits BlogPosting-only JSON-LD and its body sanitizer strips
`<script>`, so the full schema graph (Person, Organization, BreadcrumbList,
FAQPage) cannot live in the markdown. `inject_schema.py` builds it from the
same frontmatter and FAQ headings and writes it into `<head>`.

The sanitizer also drops `stroke-dasharray`, `transform`, `style` and
`aria-labelledby`. The inline charts are written to stay inside that
allowlist: the donut uses arc paths, and labels use `aria-label` plus a
`<title>` child. Editing a chart means re-checking it against `ALLOWED_ATTRS`
in `scripts/blog_render.py`.

## Before publishing

- Fill `[AUTHOR NAME]`, `[JOB TITLE]`, `[REVIEWER NAME]`, `[REVIEWER TITLE]`.
- Verify the three external citations resolve (this sandbox blocks egress, so
  Gate 5 could not check them).
- Convert `hero.png` to WebP/AVIF with a PNG fallback.
- Resolve the cannibalization actions in `reports/cannibalization-ddos-cluster.md`.
