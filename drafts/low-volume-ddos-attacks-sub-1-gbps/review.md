## Quality Review: Sub-1 Gbps Attacks: The 85% Nobody Puts on a Slide

Iteration 3 of the Blog Delivery Contract Gate 4 review (79/100 at iteration 1,
89/100 at iteration 2).

### Overall Score: 93/100 - Exceptional

| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| Content Quality | 28 | 30 | Strong, self-critical, epistemically honest; one chart weakens the evidence presentation |
| SEO Optimization | 24 | 25 | Clean hierarchy, 8 contextual internal links, 3 external primary sources; no heading anchors/TOC |
| E-E-A-T Signals | 13 | 15 | Every numeric claim named, dated and threshold-stated; author placeholders (accepted) and one distorting chart |
| Technical Elements | 14 | 15 | 5 schema types validated by Gate 3; PNG hero (accepted sandbox limit) |
| AI Citation Readiness | 14 | 15 | Self-contained passages, TL;DR box, comparison table, FAQ; no jump anchors |

### Rating: 90-100 Exceptional

Gate 3 evidence is present in `preflight-report.json` (patchright, mobile 375 /
tablet 768 / desktop 1280 / desktop-dark, zero overflows, zero console errors,
JSON-LD valid and visible-consistent at all viewports), so page speed signals and
mobile-friendliness were scored on evidence rather than marked N/A. No
reweighting of the Technical denominator was required.

### Verification notes

All six fixes claimed by the orchestrator were independently confirmed against
the artifact rather than taken on trust:

1. Chart 2 figcaption carries split attribution (Nexusguard 2025 for +69% and the
   85% share, Corero 2026 for +262%), both live anchors. Chart 3 figcaption
   carries the Corero name, date and link. The ">50% under 200 Mbps" claim is
   attributed in Key Takeaways.
2. `og_image_alt` renders to both `og:image:alt` and `<img alt>`; descriptive,
   not a title duplicate.
3. The 73% figure is attributed to the DigiCert UltraDDoS Protect 2025 Biannual
   Report with a direct link; Cloudflare Q1 2025 is linked in the table and FAQ.
   All four comparison-table rows are live links. Three distinct external domains.
4. Donut background is now two half-circle arcs covering the full ring; the data
   arc sweeps about 189 degrees, correctly encoding ">50%".
5. The Q3 2018 priority claim is softened; no priority claim remains.
6. Chart 2 axis caption present. `capabilities.json` records `markdown: true`.

### Editorial Style Diagnostics (advisory only, never authorship, never scored)

- Sentence-length variation: 0.58 (mean ~15.8 words, SD ~9.3) - descriptive only
- Configured style phrases: 0 of the listed phrases appear
- Vocabulary diversity sample: ~0.35 TTR over ~2,760 words, within the expected
  band for a long specialist piece with repeated domain terms
- Second-order review: question-cadence H2s 2 of 9 (intent-appropriate); "Here"
  openers 1 (threshold 3); false-balance framing 0; wrap-up rhetorical questions
  1; capsule H2 transitions 0; list-item word-count SD well above 5 on both lists
- Sentence-opening words skew toward "The"/"It"/"That", plausibly near the 25%
  top-three threshold
- These observations do not infer authorship and do not affect the score.

### Issues Found

#### Critical (must fix before publishing)

None. Zero P0. Every material numeric claim (85%, >50% under 200 Mbps, 962.2
Gbps, +69%, +262%, >90% under 10 minutes, six-second pulses, 99%, 96.6%, 73%, 50+
vectors) carries a named report, a publication date, a measurement threshold
where one applies, and a live URL. The iteration-2 P0 on heuristic 5 is cleared.

#### High (should fix)

- **Chart 2 axis is not proportional and mixes two vendors' figures.** Baseline
  y=215; +69% drawn 120px tall, +262% only 145px, "unchanged" 10px. At the
  implied 1.74 px/% scale, +262% should sit ~456px above the baseline. The chart
  compresses the larger number, and the direction of that distortion flatters the
  article's own thesis, which is a poor look in a post arguing that the industry
  distorts emphasis. Separately, +69% (Nexusguard, 2025) and +262% (Corero, 2026)
  are different vendors over different periods on one shared axis. Fix: rescale
  linearly, or drop the y-position encoding and render as a labelled callout with
  no implied magnitude axis. State in the caption that the two change figures are
  not a like-for-like pair.

#### Medium (recommended)

- No table of contents or heading anchor IDs on a 2,760-word, 9-H2 post.
  Heuristic 3 expects a TOC above 1,500 words, and jump anchors materially help
  AI passage extraction. `scripts/blog_hygiene.py` generates this deterministically.
- The Corero source URL is a press-release page, not the report itself, and now
  carries three separate loads (+262% peak growth, >50% under 200 Mbps, 50+
  vectors). Fix: link the underlying report, or add a retrieval note per
  heuristic 5's changeable-source rule.
- The "200 Mbps SYN flood can exhaust state" example is the one load-bearing
  technical claim with no source. Hedged with "can" and illustrative, so not a
  P0, but a citation or an explicit illustrative marker would close the gap.

#### Low (nice to have)

- Orthographic drift: "85 per cent" in the chart 2 figcaption against "85%"
  elsewhere; British "favour"/"analyses" alongside US-style formatting.
- Hero image lacks `fetchpriority="high"`. Dimensions are set and it correctly
  does not lazy-load, but the LCP hint is missing.
- Sentence-opening repetition on "The"/"It"/"That" is worth one editing pass.

### Accepted and not scored as blocking

The four `[PLACEHOLDER]` client fill-ins, the root-relative internal links, and
the PNG hero (no AVIF/WebP tooling beyond Pillow in this sandbox). These cost a
point each in author attribution and image optimization but are excluded from the
blocking decision. The placeholders appear in eight locations: frontmatter, the
byline, the About-the-author block, the reviewer line, `<meta name="author">`,
`article:author`, the Person node in JSON-LD, and the page footer.

### Prioritized Fix List

1. Rescale or de-quantify the chart 2 axis and flag the mixed-vendor comparison.
2. Add heading IDs and a TOC via `scripts/blog_hygiene.py`.
3. Point the Corero citation at the report itself, or add a retrieval date.
4. Source or explicitly mark the SYN-flood example as illustrative.
5. Normalise "per cent" vs "%" and add `fetchpriority="high"` to the hero.

None of items 1-5 is a P0, and none blocks delivery.

Nonce: a6109a509162340be48bd2b76d42f4d8
BLOCKING: false (cleared all gates; 93/100 overall, zero P0)
