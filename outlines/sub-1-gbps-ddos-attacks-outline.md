# Outline: Sub-1 Gbps Attacks, the Majority Nobody Puts on a Slide

**Site**: nexusguard.com (DDoS protection for CSPs, ISPs, MSSPs and enterprises)
**Generated**: 2026-09-16
**Ready for**: `/blog write` (after the headline-number decision below)

---

## Read This First: The 85% Figure Does Not Have a Source Yet

The working title asserts 85%. No published threat report I could find states that
number. What is actually published, as of September 2026:

| Figure | Source | Period | What it measures |
|---|---|---|---|
| 96.1% of attacks under 1 Gbps | Cloudflare DDoS Threat Report | H1 2026 | Network-layer attacks, Cloudflare network |
| 96.62% under 500 Mbps | Cloudflare DDoS Threat Report | H1 2026 | Network-layer attacks |
| 99% of L3/L4 attacks under 1 Gbps and 1 Mpps | Cloudflare | Q1 2025 | Network-layer attacks |
| ~73% of attacks between 0 and 0.5 Gbps | Corero / DigiCert UltraDDoS reporting | 2025 | Observed attacks |
| Over half of sub-1 Gbps attacks under 200 Mbps | Corero 2026 Threat Intelligence Report (2 Apr 2026) | 2026 | Sub-1 Gbps subset |
| 82%+ of incidents are small-scale, frequent, coordinated | StormWall trend reporting | since 2024 | Total recorded incidents |

Three options, in order of preference:

1. **Use Nexusguard's own telemetry.** This is the strongest play by a wide margin.
   If the Nexusguard Research Team can publish its own sub-1 Gbps share from
   platform data across 50,000-plus ASNs, the post stops being commentary on other
   vendors' reports and becomes a primary source that others cite. That is the
   entire information-gain case for this article. Pull the number before writing.
2. **Anchor to Cloudflare H1 2026 at 96.1%** and retitle. "The 96% nobody puts on a
   slide" is a stronger claim than 85%, not a weaker one.
3. **Keep 85% only if a specific report backs it.** If it came from a deck, a
   webinar or an internal dataset, name that source in the post. An unsourced
   headline number on a post whose entire thesis is "the industry misreports
   attack data" would be self-defeating.

Everything below is written to work under any of the three. Placeholder `[N]%`
marks where the chosen figure goes.

---

## Search Intent Reality Check

Be clear-eyed about what this post is. "Sub-1 Gbps attacks" is not a keyword with
meaningful search volume. The rankable head terms are `low volume DDoS attacks`,
`small DDoS attacks`, `sub-saturating DDoS`, and `short duration DDoS attacks`,
and even those are modest.

This is a **point-of-view piece whose primary channel is LinkedIn, industry press
and sales enablement**, with organic search as the long tail. That changes two
things: the title should optimize for a scroll-stopping claim rather than keyword
placement, and the post should be built so its charts and stat blocks survive
being screenshotted out of context. Write the SEO layer underneath the POV layer,
not the other way around.

---

## Title Suggestions

1. `Sub-1 Gbps Attacks: The [N]% Nobody Puts on a Slide` (POV-first, the working title; strongest for LinkedIn and press pickup)
2. `Why Low-Volume DDoS Attacks Are the Ones That Get Through` (58 chars, keyword-led, best for organic)
3. `What Is a Sub-Saturating DDoS Attack, and Why Does It Work?` (58 chars, question format for PAA and AI Overview capture)

**Recommended approach**: title 1 as the H1, with title 2's phrasing carried in the
H2 structure and meta description so the organic layer still has something to grip.

**Recommended slug**: `/blog/low-volume-ddos-attacks-sub-1-gbps`
**Meta description draft** (154 chars): `Most DDoS attacks are under 1 Gbps, short, and small enough to pass for noise. Why threat-report headlines miss them and what detection actually requires.`

---

## Target Parameters

- **Primary keyword**: low volume DDoS attacks
- **Secondary keywords**: sub-saturating DDoS, sub-1 Gbps DDoS attack, short duration DDoS, DDoS smokescreen attack, pulse wave DDoS, below-threshold DDoS detection
- **Search intent**: Informational with a strong opinion/thought-leadership overlay; commercial investigation tail for CSP and hosting-provider buyers
- **Optional planning estimate**: 1,800 to 2,200 words; deliberately shorter than a pillar page because the argument is sharper when it is tight. Not a score or gate.
- **H2 sections**: 7 plus FAQ and conclusion
- **Target reading level**: Flesch 55 to 65
- **Register note**: This post has a thesis and should sound like it. One argument, defended with data, no hedging in the opening. The competitor content in this space is uniformly neutral and forgettable.

---

## SERP and Citation Surface Analysis

**Who covers this today**

| Result | Angle | Approx. length | Weakness to exploit |
|---|---|---|---|
| Cloudflare DDoS Threat Report (quarterly, H1 2026) | The definitive dataset; 96.1% under 1 Gbps, 90.6% under 10 minutes | Long-form report | Reports the number, then leads its own headline with 1 Tbps+ growth. The contradiction this post is about. |
| Corero 2026 Threat Intelligence Report and press cycle | Sub-200 Mbps framing, six-second pulses, 50+ vector campaigns, 262% peak growth | Press release plus gated report | Gated. The best material is behind a form, leaving the free SERP thin. |
| StationX, VoxBooster, Flowtriq stat roundups | Aggregated statistics lists | 2,000 to 4,000 | Zero analysis. Pure stat aggregation, high ranking, no argument. |
| Tripwire, CSO Online, Infosecurity, Link11 (smokescreen angle) | DDoS as cover for breach and exfiltration | 800 to 1,500 | Treat the smokescreen thesis qualitatively; none connect it to the size distribution data. |
| Help Net Security, Dark Reading, TechRepublic, BleepingComputer | News coverage of each report cycle | 500 to 900 | Report-cycle churn; no durable resource. |
| Palo Alto, generic "what is DDoS" pages | Definitional | 2,000+ | Own the head term but never segment by attack size. |

**Patterns across the field**
- Every vendor publishes the size distribution and then headlines the record-breaking outlier. Nobody names that gap. It is the whole article.
- The smokescreen literature and the attack-size literature are two separate bodies of content that never cite each other. Joining them is the single best structural move available here.
- Stat-roundup pages dominate the organic results with no analysis, which is beatable on quality but not on keyword breadth.

**AI Overview and citation surface notes**
- Answer format that gets cited: a percentage with its source and period named in the same sentence.
- Repeatedly cited publishers: Cloudflare, Corero, Netscout, StationX, Help Net Security.
- Repeated entities: Gbps, Mpps, L3/L4, network layer, pulse wave, sub-saturating, threshold, scrubbing, always-on vs. on-demand, time to mitigate.
- Nexusguard is largely absent from this specific conversation despite having the telemetry to lead it.

---

## Outline

### H2: Most DDoS Attacks Are Too Small to Make the Headline (~300 words)

- **Answer-first opener**: Lead with the number and its source in the first sentence, in a form an answer engine can lift whole. `[N]% of DDoS attacks in [period] were under 1 Gbps, according to [source].` Then the turn: that figure appears in the same reports whose headlines announce record-breaking terabit attacks.
- **Key points to cover**:
  - The size distribution, stated plainly: the bulk of attacks sit under 1 Gbps, over half of those under 200 Mbps.
  - The duration distribution alongside it: more than 90% of network-layer attacks end in under 10 minutes; six-second pulses are now documented.
  - Why the headline goes to the outlier: record attacks are novel, quotable and easy to put on a slide. A 180 Mbps, 40-second flood is none of those things.
  - Set the thesis explicitly: the reporting is accurate, the emphasis is inverted, and the emphasis is what shapes procurement.
- **Key statistic to find**: The chosen headline figure plus its exact reporting period and dataset scope. Nexusguard telemetry strongly preferred.
- **Chart suggestion**: Horizontal bar. DDoS attack size distribution by band (under 200 Mbps, 200-500 Mbps, 500 Mbps to 1 Gbps, 1-10 Gbps, 10 Gbps+), with the sub-1 Gbps bands visually grouped. This is the screenshot asset. Design it to stand alone with the source baked into the image.
- **Image placement**: No. Lead with the chart.

### H2: What Counts as a Sub-Saturating Attack? (~250 words)

- **Answer-first opener**: A sub-saturating attack is one sized deliberately below the victim's link capacity and below their detection thresholds, so it degrades service or occupies defenders without ever tripping an alarm.
- **Key points to cover**:
  - Define the term and distinguish it from adjacent ones: pulse wave (repeated short bursts), carpet bombing (distributed across a prefix), low-and-slow application-layer attacks.
  - Saturation is relative. 800 Mbps is noise on a 100 Gbps peering link and an outage on a 1 Gbps customer uplink. Attack size only means something against a named denominator, which is exactly what industry headlines strip out.
  - Note the 77%-under-10-Gbps figure and who that actually breaks: hosting providers, game servers and small operators on 1 to 10 Gbps uplinks.
- **H3: Small does not mean harmless**
  - Three concrete failure modes at sub-1 Gbps: stateful device session exhaustion, customer-facing latency and packet loss inside SLA windows, and support-cost surge with no security event to point at.
- **Key statistic to find**: A published figure tying small-attack volume to actual service degradation or SLA breach, ideally from operator data rather than vendor marketing.
- **Chart suggestion**: None.
- **Image placement**: Yes. Simple diagram: same 800 Mbps attack against a 100 Gbps peering link vs. a 1 Gbps customer uplink, with the resulting utilization shown for each.

### H2: Why Threshold-Based Detection Is Built to Miss Them (~350 words)

- **Answer-first opener**: Every threshold encodes a decision about what is worth noticing. Sub-saturating attacks are engineered against that decision.
- **Key points to cover**:
  - Thresholds are tuned to avoid false positives, which means they are tuned to ignore exactly this traffic band.
  - Flow sampling: a 1:1000 sample rate and a 5-minute export interval cannot resolve a 40-second, 200 Mbps event. The telemetry pipeline loses the attack before detection logic ever sees it.
  - The reactive-mitigation gap: if detection takes 60 seconds and diversion takes another 60, a six-second pulse is over four times before anything happens. Reactive on-demand scrubbing is structurally incapable of touching this class.
  - The alert-tuning trap: operators who lower thresholds to catch these get an alert storm and re-raise them within a quarter. Name this cycle; every network team has lived it.
- **H3: What "we've never been hit" usually means**
  - The uncomfortable read: for most networks, the absence of DDoS alerts at this size is evidence about the detection configuration, not about the threat. State it directly but without condescension; the reader is the person who configured it.
- **Key statistic to find**: Published time-to-detect and time-to-mitigate benchmarks for on-demand vs. always-on deployments, attributed and dated.
- **Chart suggestion**: Line or timeline. Attack duration (6s pulse, 40s flood, 10min flood) plotted against typical detection and mitigation latency, showing which attacks finish before defense engages. Strong second screenshot candidate.
- **Image placement**: No.

### H2: The Small Attack Is Often Not the Attack (~350 words)

- **Answer-first opener**: This is the section that earns the post. The size-distribution literature and the DDoS-as-smokescreen literature have existed side by side for a decade without citing each other. Join them.
- **Key points to cover**:
  - Reconnaissance: small attacks used to fingerprint defenses, measure response time and identify which thresholds exist and where. The attacker learns your configuration by probing it.
  - Smokescreen and log flooding: DDoS events generated to bury breach indicators in alert volume, extending dwell time for credential abuse, lateral movement and exfiltration.
  - Resource diversion: NOC and SOC attention is finite; a sustained trickle of low-grade events is an effective way to spend it.
  - Extortion probing: a demonstration shot sized to prove capability without provoking a full response.
  - The reframe: at this size, treat a DDoS event as a possible signal about something else in the environment, not as an isolated availability incident. Correlate DDoS telemetry with SIEM data rather than routing it to a separate availability queue.
- **Key statistic to find**: Any published correlation between DDoS activity and subsequent breach or intrusion activity, with the study named. Be careful here: much of the smokescreen literature is assertion rather than measurement. If the evidence is thin, say so and present it as a hypothesis worth instrumenting rather than a proven pattern. Overclaiming in this section would undercut the credibility the rest of the post is built on.
- **Chart suggestion**: None. This section is argument, and a weak chart would dilute it.
- **Image placement**: Yes. Timeline showing a low-grade DDoS event overlapping a separate intrusion sequence, with the SOC alert queue shown filling in parallel.

### H2: What Detection Has to Do Instead (~350 words)

- **Answer-first opener**: Detection has to operate continuously, at line rate, on unsampled data, with automated mitigation that engages in seconds rather than minutes.
- **Key points to cover**:
  - Always-on over on-demand for this class. The diversion decision is the latency, and you cannot make it fast enough reactively.
  - Behavioral baselining per customer, per prefix and per service instead of static global thresholds.
  - Telemetry resolution: unsampled or high-rate sampling, sub-minute export, so short events survive the pipeline.
  - Correlation across time: ten 200 Mbps events against the same customer in an hour is a campaign, not ten non-events. Most systems have no concept that links them.
  - Automated mitigation with no human in the loop for the low-severity band; humans cannot be the control path at six-second timescales.
  - Multi-vector readiness: campaigns now combine dozens of vectors and adapt mid-attack, so single-signature matching is insufficient.
- **H3: Detection capability checklist**
  - Six to eight scannable, implementable checks an operator can run against their current setup this quarter. High-value for AI citation and the obvious repurposing asset for LinkedIn.
- **Key statistic to find**: Sub-second detection and mitigation benchmarks, attributed. Corero's six-second pulse finding and Nexusguard's own time-to-mitigate figures both belong here.
- **Chart suggestion**: None. The checklist carries the section.
- **Image placement**: No.

### H2: How to Read a DDoS Threat Report (~250 words)

- **Answer-first opener**: A short, genuinely useful methodology section: how to extract what matters from any vendor report, including Nexusguard's own.
- **Key points to cover**:
  - Find the size and duration distribution before reading the headline. It is usually in the report and rarely in the summary.
  - Check the denominator: whose network, which customers, which layer. A CDN's mix and a regional ISP's mix are not comparable, and neither is representative of yours.
  - Medians over maxima. The median attack tells you about your normal week; the maximum tells you about your worst day. You need both, and only one is ever on the slide.
  - Ask what the report is selling. Applies to every vendor, Nexusguard included. Saying this explicitly about your own reports is the credibility move that makes the rest of the post land.
- **Key statistic to find**: None. This section trades on candor.
- **Chart suggestion**: None.
- **Image placement**: No.

### H2: How Nexusguard Handles the Low-Volume Majority (~200 words)

- **Answer-first opener**: One sentence on the capability, then evidence. Keep this short and place it last. A post arguing that the industry oversells its headline numbers cannot end with a long sales pitch without collapsing its own thesis.
- **Key points to cover**:
  - Always-on detection posture and what it means for sub-minute events.
  - Per-customer and per-prefix behavioral baselining rather than global thresholds.
  - Platform scale as evidence of dataset breadth: 50,000-plus ASNs, 100-plus CSPs, 50-plus scrubbing centers. Verify all figures against current approved sources.
  - Time-to-detect and time-to-mitigate figures, stated as measured numbers with conditions, not as marketing claims.
- **Key statistic to find**: Current verified platform and latency figures.
- **Chart suggestion**: None.
- **Image placement**: No.
- **CTA placement**: Link to the CSP DDoS protection solution page and the latest threat report.

### Optional FAQ Section (5 items)

Mark up with FAQPage JSON-LD. Answers 40 to 60 words, each with its statistic sourced and dated inline.

1. **What percentage of DDoS attacks are under 1 Gbps?** State the chosen figure with source and period. The single most liftable answer on the page.
2. **What is a sub-saturating DDoS attack?** An attack sized below the target's link capacity and detection thresholds, degrading service or occupying defenders without triggering an alarm.
3. **Are small DDoS attacks dangerous?** Yes, in three specific ways: stateful device exhaustion, SLA-relevant latency and loss, and use as reconnaissance or cover for other activity.
4. **Why doesn't my DDoS protection detect small attacks?** Because threshold-based detection and sampled flow telemetry are tuned to ignore this band, and reactive mitigation engages after short attacks have ended.
5. **How long do most DDoS attacks last?** More than 90% of network-layer attacks end in under 10 minutes, with pulse attacks as short as six seconds. Cite source and period.

### Conclusion (~120 words)

- **Key takeaways to summarize**: The majority of DDoS activity sits below 1 Gbps and below 10 minutes. That is in every threat report and on almost no slide. The gap matters because procurement follows the slide: networks buy capacity for the attack that makes headlines and stay exposed to the one they actually get every week. Closing it is a detection-posture question, not a scrubbing-capacity question.
- **Call to action direction**: Single, low-friction CTA that matches the post's register. Run the detection capability checklist against your own setup. Secondary link to the threat report. Do not stack three CTAs on a credibility piece.

---

## Internal Linking Zones

**Link TO from this post**
- The bit-and-piece / carpet bombing post (shared thesis: attacks engineered against detection thresholds). These two are natural companions and should cross-link explicitly.
- `/resources/threat-reports` and the latest DDoS threat analysis report, linked from every Nexusguard-sourced figure.
- The CSP / service-provider DDoS protection solution page, from the final section and CTA.
- Any existing always-on vs. on-demand mitigation explainer, from the detection section.
- Any existing pulse wave or multi-vector attack explainer, from the definitions section.

**Link FROM to this post**
- The DDoS glossary, under "sub-saturating," "low-volume" and "pulse wave."
- Threat report landing pages, as the interpretive companion to the raw data.
- The bit-and-piece post, reciprocating the link above.
- Any hosting-provider or gaming-segment solution page, where sub-10 Gbps attacks are the dominant threat.

---

## Content Gaps to Exploit

1. **Naming the reporting gap itself.** Every vendor publishes the size distribution and headlines the outlier. No one has written the piece that puts those two facts next to each other. This is a first-mover position, and it is available because it requires a vendor to be mildly critical of vendor marketing, including its own.
2. **Joining the smokescreen literature to the size data.** Two mature bodies of content that have never cited each other. The synthesis is genuinely new and is the most defensible information-gain claim in the post.
3. **Attack size relative to a denominator.** Nobody normalizes attack size against victim link capacity, which is the only framing under which "small" means anything. The peering-link vs. customer-uplink comparison is a simple, original explanatory device.
4. **The duration-vs-mitigation-latency overlay.** The data for both exists separately. Charting them on one axis to show which attacks finish before defense engages has not been done in the free content on this SERP.
5. **Teaching readers to audit vendor reports, including Nexusguard's.** Unusual, memorable, and disproportionately effective at building the trust that makes the final section believable.
6. **Format advantages available**: two standalone screenshot-grade charts with embedded sourcing, a detection checklist, FAQPage schema, and a genuine thesis in a field of neutral stat roundups.

---

## Pre-Publication Notes

- **Resolve the headline number first.** Do not draft until the `[N]%` decision is made, since the title, opening paragraph, chart and lead FAQ all depend on it. See the table at the top.
- **Fact-check gate.** Every figure must carry source and period inline. The post's thesis is about statistical honesty, so an unsourced or stale number does disproportionate damage here. Run `/blog factcheck` and treat any UNVERIFIED flag as blocking rather than advisory.
- **Tone review before publish.** The argument requires criticizing an industry norm Nexusguard participates in. It should read as self-aware, not as competitor-bashing. Do not name rival vendors in a critical frame; cite their data approvingly and criticize the shared convention. Worth a marketing and legal read.
- **Cannibalization**: low risk against existing Nexusguard content, but check for overlap with any published pulse-wave or always-on mitigation posts. Run `/blog cannibalization`.
- **Schema to generate**: BlogPosting plus FAQPage plus BreadcrumbList. Named researcher byline with credentials, not a company byline.
- **Distribution plan**: this post is built for `/blog repurpose`. The size-distribution chart and the detection checklist are the two assets; LinkedIn and industry press are the primary channels, organic search is the tail.
- **Suggested next commands**: `/blog write` (after the number is resolved), `/blog chart` (two charts), `/blog schema`, `/blog factcheck`, `/blog seo-check`, `/blog repurpose`.
