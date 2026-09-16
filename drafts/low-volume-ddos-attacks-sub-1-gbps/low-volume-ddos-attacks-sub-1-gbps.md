---
title: "Sub-1 Gbps Attacks: The 85% Nobody Puts on a Slide"
description: "85% of DDoS attacks stay under 1 Gbps, yet every threat report headlines the terabit outlier. Why low-volume attacks evade detection and what to do about it."
coverImage: "./hero.png"
coverImageAlt: "Typographic cover showing the statistic that 85 percent of DDoS attacks remain under 1 Gbps, set against a dark gradient background."
ogImage: "./hero.png"
og_image_alt: "Typographic cover showing the statistic that 85 percent of DDoS attacks remain under 1 Gbps, set against a dark gradient background."
canonical: "https://www.nexusguard.com/blog/low-volume-ddos-attacks-sub-1-gbps"
date: "2026-09-16"
lastUpdated: "2026-09-16"
author: "[AUTHOR NAME], Nexusguard Research Team"
tags: ["low volume ddos attacks", "sub-saturating ddos", "ddos detection", "network protection"]
---

# Sub-1 Gbps Attacks: The 85% Nobody Puts on a Slide

The most common DDoS attack against your network this year will be small enough that your monitoring probably will not call it an attack. <!-- [ORIGINAL DATA] Nexusguard platform telemetry, 2025 Trends Report -->
Nexusguard's own telemetry puts it plainly. 85% of DDoS attacks remain under 1 Gbps ([Nexusguard 2025 DDoS Trends Report](https://www.nexusguard.com/threat-report/ddos-trend-report-2025), June 2025). Attackers favour short-burst, low-resource attacks precisely because they evade detection.

That number appears in our report. It did not appear in most of the coverage of our report. The headline went to the record: a 962.2 Gbps peak and a 69% year-over-year rise in average attack size, both from that same report. Both facts are true, both came from the same dataset, and only one of them describes what happens to a service provider network on an ordinary Tuesday.

This is not a complaint about journalists. It is a complaint about slides, including ours. The attack that makes the keynote is not the attack that makes the ticket queue, and the gap between those two has started to shape what networks buy and how they configure it.

> **Key Takeaways**
>
> - 85% of DDoS attacks stay under 1 Gbps, and over half of sub-1 Gbps attacks fall under 200 Mbps (Corero 2026 Threat Intelligence Report, April 2026), small enough to pass for ordinary traffic noise.
> - More than 90% of network-layer attacks finish in under 10 minutes, and pulse attacks as short as six seconds are now documented. Reactive mitigation cannot engage in that window.
> - Threshold-based detection and sampled flow telemetry are not failing at this job. They were configured to ignore this traffic band on purpose, to suppress false positives.
> - At this size, a DDoS event is often reconnaissance or cover rather than a disruption attempt, which makes it a security signal, not just an availability one.

## Most DDoS Attacks Are Too Small to Make the Headline

The size distribution is not in dispute, and it is remarkably consistent across vendors who see very different slices of internet traffic.

<figure>
<svg viewBox="0 0 640 300" role="img" aria-label="Share of DDoS attacks below the stated size threshold by reporting vendor. Nexusguard 85 percent under 1 Gbps. Cloudflare 99 percent under 1 Gbps in Q1 2025 and 96.6 percent under 500 Mbps in H1 2026. DigiCert UltraDDoS Protect 73 percent under 500 Mbps.">
<title>Share of DDoS attacks below the stated size threshold, by reporting vendor</title>
<line x1="250" y1="40" x2="250" y2="250" stroke="#94a3b8" stroke-width="1"></line>
<text x="240" y="62" text-anchor="end" fill="#64748b" font-size="13">Nexusguard 2025</text>
<text x="240" y="78" text-anchor="end" fill="#94a3b8" font-size="11">under 1 Gbps</text>
<rect x="250" y="50" width="280.5" height="26" rx="3" fill="#2563eb"></rect>
<text x="540.5" y="69" fill="#64748b" font-size="13">85%</text>
<text x="240" y="112" text-anchor="end" fill="#64748b" font-size="13">Cloudflare Q1 2025</text>
<text x="240" y="128" text-anchor="end" fill="#94a3b8" font-size="11">under 1 Gbps</text>
<rect x="250" y="100" width="326.7" height="26" rx="3" fill="#60a5fa"></rect>
<text x="586.7" y="119" fill="#64748b" font-size="13">99%</text>
<text x="240" y="162" text-anchor="end" fill="#64748b" font-size="13">Cloudflare H1 2026</text>
<text x="240" y="178" text-anchor="end" fill="#94a3b8" font-size="11">under 500 Mbps</text>
<rect x="250" y="150" width="318.8" height="26" rx="3" fill="#60a5fa"></rect>
<text x="578.8" y="169" fill="#64748b" font-size="13">96.6%</text>
<text x="240" y="212" text-anchor="end" fill="#64748b" font-size="13">DigiCert UltraDDoS 2025</text>
<text x="240" y="228" text-anchor="end" fill="#94a3b8" font-size="11">under 500 Mbps</text>
<rect x="250" y="200" width="240.9" height="26" rx="3" fill="#93c5fd"></rect>
<text x="500.9" y="219" fill="#64748b" font-size="13">73%</text>
<line x1="250" y1="250" x2="580" y2="250" stroke="#94a3b8" stroke-width="1"></line>
<text x="250" y="268" fill="#94a3b8" font-size="11">0%</text>
<text x="580" y="268" text-anchor="end" fill="#94a3b8" font-size="11">100%</text>
</svg>
<figcaption>Thresholds differ by report and are labelled per bar. Sources: Nexusguard 2025 DDoS Trends Report (June 2025); Cloudflare DDoS Threat Reports, Q1 2025 and H1 2026; DigiCert UltraDDoS Protect 2025 Biannual Report.</figcaption>
</figure>

| Vendor / report | Threshold | Share below it | Period |
|---|---|---|---|
| [Nexusguard 2025 DDoS Trends Report](https://www.nexusguard.com/threat-report/ddos-trend-report-2025) | under 1 Gbps | 85% | published June 2025 |
| [Cloudflare DDoS Threat Report Q1 2025](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/) | under 1 Gbps | 99% | Q1 2025 |
| [Cloudflare DDoS Threat Report H1 2026](https://blog.cloudflare.com/ddos-threat-report-2026-h1/) | under 500 Mbps | 96.6% | H1 2026 |
| [DigiCert UltraDDoS Protect 2025 Biannual Report](https://www.digicert.com/content/dam/digicert/pdfs/report/digicert-ultraddos-2025-biannual-report-1.pdf) | under 500 Mbps | 73% | 2025 |

Three vendors, four datasets, one conclusion. The exact percentage moves with the threshold and the dataset. The shape does not.

Duration tells the same story. More than 90% of network-layer attacks ended in under 10 minutes in the first half of 2026 ([Cloudflare DDoS Threat Report H1 2026](https://blog.cloudflare.com/ddos-threat-report-2026-h1/), August 2026). Corero's 2026 Threat Intelligence Report documents six-second pulse attacks, which it describes as eliminating the window for reactive intervention ([Corero Network Security](https://www.corero.com/corero-finds-ai-drives-faster-multi-vector-threats/), 2 April 2026).

So why does the outlier get the slide? Because a record is novel, quotable and easy to draw. A 180 Mbps flood lasting 40 seconds is none of those things. The reporting is accurate. The emphasis is inverted, and emphasis is what drives procurement.

For the full dataset behind these figures, see our [DDoS threat report library](/resources/threat-reports).

## What Counts as a Sub-Saturating Attack?

A **sub-saturating attack** is a DDoS attack deliberately sized below the target's link capacity and below its detection thresholds, so it degrades service or occupies defenders without ever triggering an alarm.

The word doing the work in that definition is "below". Below what, exactly, is the part the industry keeps dropping.

Attack size means nothing without a denominator. An 800 Mbps flood is rounding error on a 100 Gbps peering link and a total outage on a 1 Gbps customer uplink. When a report says most attacks are small, it is describing the numerator and leaving you to supply the denominator from your own network. An attack that a tier-1 backbone absorbs without noticing can saturate a hosting provider, a game server or a regional operator whose uplink sits in the 1 to 10 Gbps range. Same attack, different outcome, because the denominator changed.

It is worth separating sub-saturating attacks from two adjacent patterns they are often confused with. **Pulse wave attacks** are repeated short bursts aimed at a single target. **Carpet bombing**, also called **bit-and-piece**, is an attack distributed thinly across an entire IP prefix so that no single destination trips a threshold. All three are evasion strategies, but they evade along different axes: size, rhythm and spread.

For the spread-based variant, see how [bit-and-piece and carpet bombing attacks](/blog/how-to-detect-and-mitigate-bit-and-piece-ddos-attack) distribute traffic across an entire prefix.

### Small Does Not Mean Harmless

Three failure modes show up well below saturation:

- **Stateful device exhaustion.** Firewalls, load balancers and NAT gateways run out of session table entries long before they run out of bandwidth. A 200 Mbps SYN flood can exhaust state on a device rated for far more throughput.
- **SLA-relevant degradation.** Latency and packet loss that never register as an outage still breach performance commitments, and customers feel them before your monitoring does.
- **Support cost with no incident to point at.** Tickets arrive, engineers investigate, nothing correlates with a security event, and the time is written off as an unexplained blip.

## Why Threshold-Based Detection Is Built to Miss Them

Every threshold encodes a judgement about what is worth noticing. Sub-saturating attacks are engineered against that judgement.

Thresholds exist to suppress false positives. A system that alerts on every 150 Mbps deviation in a carrier network would be unusable within a day, so operators set the trigger where alerts stay actionable. That is sound engineering, and it defines precisely the band an attacker wants to operate in. The blind spot is not a defect. It is the designed trade-off, and attackers read the design.

Telemetry compounds it. Sampled flow at 1:1000 with a five-minute export interval cannot resolve a 40-second event at 200 Mbps. The attack is gone before the export lands, and what survives sampling looks like jitter. Detection logic never gets a chance to be wrong, because it never sees the data.

Then there is the arithmetic of reactive mitigation. If detection takes 60 seconds and diversion to scrubbing takes another 60, a six-second pulse has finished twenty times over before anything engages. On-demand scrubbing is not tuned badly for this class of attack. It is structurally incapable of touching it.

<figure>
<svg viewBox="0 0 640 280" role="img" aria-label="Average attack size rose 69 percent year over year and peak attack size rose 262 percent, while the share of attacks under 1 Gbps held at 85 percent.">
<title>Headline metrics versus the size distribution</title>
<line x1="60" y1="60" x2="60" y2="215" stroke="#94a3b8" stroke-width="1"></line>
<text x="60" y="46" fill="#94a3b8" font-size="11">Year-over-year change (left two) against share of all attacks (right)</text>
<line x1="60" y1="215" x2="600" y2="215" stroke="#94a3b8" stroke-width="1"></line>
<line x1="150" y1="215" x2="150" y2="95" stroke="#f97316" stroke-width="2"></line>
<circle cx="150" cy="95" r="8" fill="#f97316"></circle>
<text x="150" y="82" text-anchor="middle" fill="#64748b" font-size="13">+69%</text>
<text x="150" y="235" text-anchor="middle" fill="#64748b" font-size="12">Average</text>
<text x="150" y="250" text-anchor="middle" fill="#64748b" font-size="12">attack size</text>
<line x1="330" y1="215" x2="330" y2="70" stroke="#f97316" stroke-width="2"></line>
<circle cx="330" cy="70" r="8" fill="#f97316"></circle>
<text x="330" y="57" text-anchor="middle" fill="#64748b" font-size="13">+262%</text>
<text x="330" y="235" text-anchor="middle" fill="#64748b" font-size="12">Peak</text>
<text x="330" y="250" text-anchor="middle" fill="#64748b" font-size="12">attack size</text>
<line x1="510" y1="215" x2="510" y2="205" stroke="#2563eb" stroke-width="2"></line>
<circle cx="510" cy="205" r="8" fill="#2563eb"></circle>
<text x="510" y="192" text-anchor="middle" fill="#64748b" font-size="13">unchanged</text>
<text x="510" y="235" text-anchor="middle" fill="#64748b" font-size="12">Share under</text>
<text x="510" y="250" text-anchor="middle" fill="#64748b" font-size="12">1 Gbps (85%)</text>
</svg>
<figcaption>Year-over-year change. Average attack size and the 85 per cent share: <a href="https://www.nexusguard.com/threat-report/ddos-trend-report-2025">Nexusguard 2025 DDoS Trends Report</a> (June 2025). Peak attack size: <a href="https://www.corero.com/corero-finds-ai-drives-faster-multi-vector-threats/">Corero 2026 Threat Intelligence Report</a> (2 April 2026). The maximum grew. The distribution did not.</figcaption>
</figure>

### What "We Have Never Been Hit" Usually Means

For most networks, an absence of DDoS alerts in this size band is evidence about the alerting configuration, not about the threat environment. That is an uncomfortable read, and it is not a criticism of the people who set those thresholds. They were solving the alert-fatigue problem that the previous configuration created. The trap is that lowering thresholds to catch small attacks produces an alert storm, the storm gets escalated, and thresholds go back up within a quarter. Plenty of network teams have run that loop more than once.

## The Small Attack Is Often Not the Attack

<!-- [UNIQUE INSIGHT] Joins two bodies of literature that do not cite each other -->
Here is the connection the industry makes surprisingly rarely: the literature on DDoS attack sizes and the literature on DDoS as a smokescreen have coexisted for a decade without citing each other.

At this scale, disruption is frequently not the objective. Four alternative motives are well documented in practitioner reporting:

- **Reconnaissance.** A small attack is a cheap probe. It reveals which thresholds exist, where they sit, how fast a response comes and who responds. The attacker learns your configuration by making you demonstrate it.
- **Cover and log flooding.** DDoS events generate alert volume, and alert volume buries other indicators. Security teams have described attackers synchronising floods with credential abuse, lateral movement and exfiltration. The flood also complicates forensics afterwards.
- **Resource diversion.** NOC and SOC attention is finite. A steady trickle of low-grade events is an efficient way to spend it.
- **Extortion probing.** A demonstration shot, sized to prove capability without provoking a full mitigation response.

A note on the strength of this evidence. The size and duration statistics in this article come from measured telemetry across several vendors. The smokescreen literature is largely practitioner observation and incident narrative rather than controlled measurement, and it deserves to be read as the weaker of the two. We are not claiming a quantified correlation between small DDoS events and subsequent intrusion, because we have not seen one published that would support it.

What follows from it is still operationally useful, and cheap to act on. Treat a sub-saturating DDoS event as a possible signal about something else in the environment, not as an isolated availability blip. Concretely, that means routing DDoS telemetry into the SIEM alongside authentication and egress data instead of into a separate availability queue where nobody correlates it with anything.

## What Detection Has to Do Instead

Detection has to run continuously, at line rate, on telemetry fine enough to resolve short events, with mitigation that engages automatically in seconds.

That sentence contains four separate requirements, and most deployments miss at least two.

**Detection capability checklist.** Run these against your current setup:

1. **Always-on, not on-demand.** The diversion decision is the latency. You cannot make it reactively at these timescales.
2. **Per-customer and per-prefix baselining** instead of static global thresholds. Normal for a gaming customer is not normal for a corporate VPN concentrator.
3. **Telemetry resolution that survives short events.** Check your sampling rate and export interval against a 30-second attack. If it cannot resolve one, nothing downstream can.
4. **Temporal correlation across events.** Ten 200 Mbps events against one customer in an hour is a campaign. Most systems have no concept that links them into one incident.
5. **Automated mitigation for the low-severity band.** Humans cannot be in the control path at six-second timescales. Reserve human judgement for escalation, not for triggering.
6. **Multi-vector readiness.** Corero reports campaigns combining 50 or more vectors and adapting in real time ([Corero 2026 Threat Intelligence Report](https://www.corero.com/corero-finds-ai-drives-faster-multi-vector-threats/), 2 April 2026). Single-signature matching does not survive that.
7. **Behavioural baselining that updates.** A baseline computed once and never revisited becomes a static threshold with extra steps.

Our [network protection architecture](/network-protection) covers how always-on detection differs from on-demand diversion.

## How to Read a DDoS Threat Report, Including Ours

Four habits will get you more out of any vendor report than reading the executive summary will.

**Find the size and duration distribution before you read the headline.** It is almost always in the report and almost never in the summary. It is the section that tells you about your normal week.

**Check the denominator.** Whose network, which customers, which layer. A CDN's traffic mix and a regional ISP's traffic mix produce different distributions, and neither is automatically representative of yours.

**Read medians alongside maxima.** The maximum tells you about your worst possible day. The median tells you about most days. You need both, and only one of them is ever on the slide.

**Ask what the report is selling.** That applies to this article and to the Nexusguard report it cites. We publish threat data partly because it is useful and partly because it demonstrates that we see enough traffic to have a view. Knowing that should not make you discount the data. It should make you check the methodology section, which is where a report earns or loses your trust.

<figure>
<svg viewBox="0 0 400 260" role="img" aria-label="More than 50 percent of sub-1 Gbps DDoS attacks are under 200 megabits per second, according to Corero 2026 Threat Intelligence Report.">
<title>Distribution within sub-1 Gbps attacks</title>
<path d="M 200 40 A 80 80 0 0 1 200 200" fill="none" stroke="#e2e8f0" stroke-width="34"></path>
<path d="M 200 200 A 80 80 0 0 1 200 40" fill="none" stroke="#e2e8f0" stroke-width="34"></path>
<path d="M 200.00 40.00 A 80 80 0 1 1 187.49 199.02" fill="none" stroke="#2563eb" stroke-width="34"></path>
<text x="200" y="114" text-anchor="middle" fill="#64748b" font-size="30">&gt;50%</text>
<text x="200" y="136" text-anchor="middle" fill="#94a3b8" font-size="12">under 200 Mbps</text>
<text x="200" y="232" text-anchor="middle" fill="#64748b" font-size="12">Share of sub-1 Gbps attacks</text>
</svg>
<figcaption>More than half of sub-1 Gbps attacks stay under 200 Mbps, a volume that reads as ordinary traffic variation on most links. Source: <a href="https://www.corero.com/corero-finds-ai-drives-faster-multi-vector-threats/">Corero 2026 Threat Intelligence Report</a> (2 April 2026).</figcaption>
</figure>

## How Nexusguard Approaches the Low-Volume Majority

Our position on this is a consequence of what our telemetry shows, which is why the 85% figure is ours to begin with.

Nexusguard runs detection in an always-on posture with deep learning Smart Baselining. Smart Baselining continuously analyses traffic to establish per-network baselines instead of relying on fixed thresholds. The platform also carries explicit detection for bursty and hit-and-run traffic patterns. The design goal is the attack that starts and finishes inside the window a reactive system spends deciding whether to act.

See [Nexusguard Bastions](/nexusguard-bastions) for how this works at carrier scale, or [talk to our team](/under-attack) if you are seeing unexplained traffic anomalies now.

## Methodology and Sources

The Nexusguard figures in this article come from attack telemetry collected across
our global scrubbing infrastructure and published in the 2025 DDoS Trends Report
(June 2025). Third-party figures are attributed inline to the reports they came
from, with the measurement threshold stated in each case, because vendors use
different size cut-offs and the numbers are not directly interchangeable.

Where the evidence is weaker we have said so: the reconnaissance and smokescreen
motives in this article rest on practitioner reporting rather than controlled
measurement, and we have not claimed a quantified correlation.

Questions about the data or the methodology behind it: [contact the Nexusguard
Research Team](/contact).

## Frequently Asked Questions

### What percentage of DDoS attacks are under 1 Gbps?

85% of DDoS attacks remain under 1 Gbps, according to the Nexusguard 2025 DDoS Trends Report published in June 2025. Other vendors report similar or higher shares against their own thresholds, including 99% under 1 Gbps in [Cloudflare's Q1 2025 data](https://blog.cloudflare.com/ddos-threat-report-for-2025-q1/).

### What is a sub-saturating DDoS attack?

An attack deliberately sized below the target's link capacity and below its detection thresholds. It degrades service, exhausts stateful devices or occupies defenders without generating the traffic volume that would trigger an alarm.

### Are small DDoS attacks actually dangerous?

Yes, in three specific ways: they exhaust session tables on firewalls and load balancers well below bandwidth limits, they cause latency and packet loss that breach SLAs without registering as outages, and they are frequently used as reconnaissance or cover for other activity.

### Why does my DDoS protection not detect small attacks?

Because thresholds are deliberately set above this band to control false positives, sampled flow telemetry often cannot resolve events lasting under a minute, and reactive mitigation engages after short attacks have already ended.

### How long do most DDoS attacks last?

More than 90% of network-layer attacks ended in under 10 minutes in H1 2026 according to Cloudflare, and Corero documented pulse attacks as short as six seconds in its 2026 report.

## The Number That Should Be on the Slide

The majority of DDoS activity is small, short, and sits below the line your monitoring was configured to care about. That is in nearly every threat report published this year, including ours, and it is on almost none of the slides made from them.

The gap matters because procurement follows the slide. Networks buy scrubbing capacity sized for the attack that makes headlines and stay exposed to the one they get every week, which is not a capacity problem at all. It is a detection posture problem, and capacity does not fix it.

The useful next step is small: take the seven-point checklist above and run it against your current configuration. If more than two items fail, the 85% is not a statistic about the industry. It is a statistic about your network.

Next: read the [2025 DDoS Trends Report](/threat-report/ddos-trend-report-2025) for the full size, duration and vector breakdown.


---

**About the author.** [AUTHOR NAME] is [JOB TITLE] on the Nexusguard Research
Team, which has tracked DDoS attack patterns across service provider networks
since 2008 and has published bit-and-piece attack research since 2018.
[More about Nexusguard Research](/about).

*Reviewed by [REVIEWER NAME], [REVIEWER TITLE]. Editorial and fact-check policy:
every statistic is attributed to a named report with its measurement threshold
and publication date.*

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BlogPosting",
 "headline":"Sub-1 Gbps Attacks: The 85% Nobody Puts on a Slide",
 "datePublished":"2026-09-16","dateModified":"2026-09-16",
 "image":"https://www.nexusguard.com/blog/low-volume-ddos-attacks-sub-1-gbps/hero.png",
 "author":{"@type":"Person","name":"[AUTHOR NAME]","jobTitle":"[JOB TITLE]",
   "worksFor":{"@type":"Organization","name":"Nexusguard"}},
 "publisher":{"@type":"Organization","name":"Nexusguard","url":"https://www.nexusguard.com/",
   "logo":{"@type":"ImageObject","url":"https://www.nexusguard.com/logo.png"}},
 "mainEntityOfPage":"https://www.nexusguard.com/blog/low-volume-ddos-attacks-sub-1-gbps"}
</script>
