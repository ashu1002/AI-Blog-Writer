# Cannibalization Report: DDoS Attack-Pattern Cluster (nexusguard.com)

**Date**: 2026-09-16
**Mode**: Local (SERP-supplemented)
**API mode**: `SKIPPED: DataForSEO wrapper unavailable` (no wrapper in `scripts/`, `DATAFORSEO_LOGIN` unset)

## Corpus

Local scan of the repo found 2 content files, both planned outlines. Neither is
published, so a local-only analysis would have nothing meaningful to compare.
The actual cannibalization risk is against **published nexusguard.com content**,
which is not in this repo.

`www.nexusguard.com` is blocked by this environment's egress proxy, so the
published inventory below was assembled from search-result titles and URLs
rather than by fetching and parsing each page. Treat keyword extraction for
published pages as inferred from title and URL only, not from full page content.
Confirm against the live pages or a sitemap crawl before acting on any
recommendation marked CRITICAL.

### Published inventory (inferred)

| ID | URL | Inferred primary keyword |
|---|---|---|
| P1 | `/blog/detecting-and-mitigating-the-increasing-threat-of-bit-and-piece-attacks` | detect mitigate bit-and-piece attacks |
| P2 | `/blog/how-to-detect-and-mitigate-bit-and-piece-ddos-attack` | detect mitigate bit-and-piece ddos attack |
| P2b | `blog.nexusguard.com/how-to-detect-and-mitigate-bit-and-piece-ddos-attack` | (duplicate of P2 on second host) |
| P3 | `/blog/attackers-continue-to-derive-new-attack-patterns-using-the-bit-and-piece-framework` | bit-and-piece framework attack patterns |
| P4 | `/promo-2023-carpet-bombing` | carpet bombing defense network providers |
| P5 | `/promo-2024-carpet-bombing` | carpet bombing defense network providers |
| P6 | `/promo-2024q3-carpet-bombing` | carpet bombing ddos defense |
| P7 | `blog.nexusguard.com/tag/bit-and-piece` | bit-and-piece (tag archive) |
| P8 | `/threat-report/ddos-trend-report-2025` | ddos trends report 2025 |
| P9 | `/blog/preventing-slow-http-attacks` | slow http attacks |

### Planned (this repo)

| ID | File | Primary keyword |
|---|---|---|
| D1 | `outlines/bit-and-piece-carpet-bombing-attacks-outline.md` | bit-and-piece and carpet bombing attacks |
| D2 | `outlines/sub-1-gbps-ddos-attacks-outline.md` | low volume DDoS attacks |

---

## Summary Table

| Post A | Post B | Shared keywords | Severity | Recommendation |
|---|---|---|---|---|
| P1 | P2 | detect, mitigate, bit-and-piece, DDoS attack | Critical | MERGE |
| P2 | P2b | entire page (two hosts) | Critical | CANONICAL |
| D1 | P1 | bit-and-piece, carpet bombing, detect, mitigate | Critical | MERGE (D1 becomes pillar) |
| D1 | P2 | bit-and-piece, carpet bombing, detect, mitigate | Critical | MERGE (D1 becomes pillar) |
| P4 | P5 | carpet bombing, network providers, defense | Critical | MERGE |
| P5 | P6 | carpet bombing, DDoS, defense | Critical | MERGE |
| D1 | P4/P5/P6 | carpet bombing DDoS | High | DIFFERENTIATE (editorial vs. commercial intent) |
| D1 | P3 | bit-and-piece, attack patterns | High | DIFFERENTIATE |
| D1 | D2 | below-threshold detection, evasion, DDoS | Medium | DIFFERENTIATE |
| D2 | P8 | DDoS attack size, under 1 Gbps | Low | NO ACTION |
| D1 | P7 | bit-and-piece (tag archive) | Low | NO ACTION |
| D1/D2 | P9 | DDoS, detection | Low | NO ACTION |

---

## Cluster 1: Bit-and-Piece Editorial (CRITICAL)

**Members**: P1, P2, P2b, P3, and planned D1.

Four or five URLs targeting effectively one keyword. P1 and P2 are the worst
offenders: both are "detect and mitigate bit-and-piece" pages, differing mainly
in title phrasing. This cannibalization **already exists** and predates the
planned post. D1 would make it a fifth competing URL.

**Which is stronger**: unknown without rankings data. P1 surfaced first in
generic searches, suggesting it currently carries the authority, but confirm in
Search Console (compare impressions, clicks and average position for
`bit and piece ddos` and `carpet bombing ddos` across all four URLs) before
choosing the survivor.

**Recommendation: MERGE, with D1 as the destination.**

1. Publish D1 at `/blog/bit-and-piece-carpet-bombing-attacks` as the pillar.
2. 301 P1 and P2 into it. Port any unique technical detail from both into D1
   first; the 2018-2019 originals may contain first-hand research detail worth
   preserving, and that detail is the E-E-A-T asset.
3. Keep P3 (attack-pattern evolution) as a genuinely distinct angle, but retitle
   away from the head term and link it up to D1. See Cluster 4.
4. Preserve every internal link pointing at P1 or P2 by repointing to D1.
5. Rebuild the tag archive P7 to list D1 first.

**Do not publish D1 until this is decided.** Adding a fifth URL to an already
split cluster is the one outcome worse than the status quo.

---

## Cluster 2: Host Duplication (CRITICAL, and bigger than it looks)

**Members**: `www.nexusguard.com/blog/...` and `blog.nexusguard.com/...`

The same articles appear on both hosts. Search results also surfaced indexed
pagination-parameter URLs (`?beb2360f_page=2`, `?26342806_page=2`), which
multiply the duplicate surface further.

This is not keyword cannibalization in the ordinary sense. It is full-page
duplication across two hostnames, and it affects **every** post on the blog, not
just this cluster. Left unfixed, it will blunt the merge in Cluster 1: 301ing
P1 and P2 on `www` achieves little if `blog.nexusguard.com` still serves them.

**Recommendation: CANONICAL, as a site-wide task.**

1. Pick one canonical host. `www.nexusguard.com/blog/` is the likely choice,
   since it consolidates authority with the main domain.
2. Self-referencing canonicals on the chosen host; cross-domain canonicals or
   301s from the other.
3. Add `rel="canonical"` on paginated parameter URLs pointing at the unparameterized
   page, or handle via parameter rules.
4. Verify in Search Console which host currently holds the impressions before
   choosing, since redirecting the stronger host into the weaker one would cost
   real traffic.

This is out of scope for a blog-post decision and belongs to whoever owns the
site architecture. Flagging it because it materially changes the value of
everything else in this report.

---

## Cluster 3: Carpet Bombing Promo Pages (CRITICAL)

**Members**: P4 (`promo-2023`), P5 (`promo-2024`), P6 (`promo-2024q3`).

Three campaign landing pages on the same offer, two sharing an almost identical
title. Dated promo URLs accumulating year over year is a common and easily fixed
pattern.

**Recommendation: MERGE into one evergreen page.**

1. Create `/carpet-bombing-protection` (undated) as the single commercial page.
2. 301 all three promo URLs into it.
3. If campaign-specific landing pages are needed for paid traffic, keep them
   `noindex` so they never enter the organic index. Paid landing pages have no
   reason to compete organically.

---

## Cluster 4: Editorial vs. Commercial Intent (HIGH)

**Members**: D1 vs. the merged carpet bombing commercial page; D1 vs. P3.

Once Clusters 1 and 3 are resolved, D1 (informational) and the evergreen promo
page (transactional) still share the head term `carpet bombing ddos`.

**Recommendation: DIFFERENTIATE.** This pairing is healthy if the targeting is
deliberate:

- D1 targets informational: `what is carpet bombing ddos`, `bit-and-piece attack`,
  `how to detect carpet bombing`.
- The commercial page targets transactional: `carpet bombing ddos protection`,
  `carpet bombing mitigation solution`, `ddos protection for network providers`.
- Cross-link explicitly: D1 links down to the solution page from its final
  section; the solution page links up to D1 as the technical explainer.

For **P3**, retitle around the evolution angle (attack-pattern changes over time,
new variants since 2018) rather than the head term, and link it to D1. It has a
legitimately distinct angle that the current title buries under the shared keyword.

---

## Cluster 5: D1 vs. D2, the Two Planned Posts (MEDIUM)

Both posts argue that attacks are engineered to sit below detection thresholds.
That shared thesis is deliberate and was flagged in both outlines. The overlap is
real but manageable.

**Recommendation: DIFFERENTIATE**, with the split drawn on the axis of evasion:

- **D1 (carpet bombing)**: evasion by **distribution**. Attack spread across many
  destinations. Unit of analysis is the prefix.
- **D2 (sub-1 Gbps)**: evasion by **size and duration**. Attack small and short on
  a single destination. Unit of analysis is the time window.

Concrete guardrails for the drafts:
- D2 should reference carpet bombing only once, as a named adjacent pattern, and
  link to D1 rather than re-explaining it.
- D1 should not argue the "industry headlines the outlier" thesis at all. That
  belongs to D2 exclusively.
- Do not duplicate the threshold-evasion explanation. D1 owns the prefix-level
  version, D2 owns the size-and-duration version.
- Publish D1 first. It is the definitional pillar, and D2's argument lands better
  once the reader can be pointed at a concrete evasion pattern.

---

## Cluster 6: D2 vs. Threat Reports (LOW, NO ACTION)

D2 interprets data that P8 and its siblings publish. Different intent (analysis
vs. data download), different SERP, and the relationship is mutually reinforcing:
D2 cites P8, P8 gains a linking asset.

Documented reasoning for future audits: monitor quarterly. If D2 begins
outranking the report landing pages for `ddos attack statistics` style queries,
revisit, since report pages are the conversion asset there.

---

## Prioritized Action Queue

| # | Action | Severity | Owner | Blocking D1? |
|---|---|---|---|---|
| 1 | Pull Search Console data for P1, P2, P2b, P3 on the bit-and-piece cluster | Critical | SEO | Yes |
| 2 | Decide pillar URL and 301 map for Cluster 1 | Critical | SEO + content | Yes |
| 3 | Resolve `www` vs. `blog` host duplication | Critical | Web / dev | No, but degrades everything |
| 4 | Consolidate three carpet bombing promo pages | Critical | Marketing | No |
| 5 | Retitle P3 to the evolution angle | High | Content | No |
| 6 | Set D1/D2 keyword split per Cluster 5 before drafting | Medium | Content | Yes for D2 |
| 7 | Rebuild bit-and-piece tag archive ordering | Low | Content | No |

Items 1, 2 and 6 gate the drafting work. Items 3, 4, 5 and 7 can run in parallel.

---

## Method Limitations

- Published-page keywords are inferred from titles and URLs only. Page content
  was not fetched (egress blocked), so H2-level overlap is unverified.
- No ranking, impression or search-volume data. Severity here reflects keyword
  and intent overlap, not measured SERP competition. The Search Console pull in
  action 1 is what turns these from hypotheses into decisions.
- The published inventory is what search surfaced, not a complete crawl. There
  may be further bit-and-piece or carpet bombing URLs not listed. A sitemap crawl
  would close this gap.
- Re-run with `--api` once a DataForSEO wrapper exists to get Page Intersection
  data for the P1/P2/P3 triad, which is where the severity formula would be most
  informative.
