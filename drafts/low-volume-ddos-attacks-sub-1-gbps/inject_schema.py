"""Inject the full schema graph into the rendered HTML head.

blog_render.py emits BlogPosting only, and its body sanitizer strips <script>,
so the Person/Organization/BreadcrumbList/FAQPage graph cannot live in the
markdown. It is built here from the same frontmatter + FAQ headings instead.
"""
import json, pathlib, re

SLUG = "low-volume-ddos-attacks-sub-1-gbps"
URL = "https://www.nexusguard.com/blog/" + SLUG
html = pathlib.Path(SLUG + ".html").read_text()
md = pathlib.Path(SLUG + ".md").read_text()

faqs = re.findall(r'^### (.+?)\n\n(.+?)(?=\n\n)', md.split("## Frequently Asked Questions")[1], re.S | re.M)

graph = {
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "BlogPosting",
         "@id": URL + "#post",
         "headline": "Sub-1 Gbps Attacks: The 85% Nobody Puts on a Slide",
         "description": "85% of DDoS attacks stay under 1 Gbps, yet every threat report headlines the terabit outlier. Why low-volume attacks evade detection and what to do about it.",
         "image": URL + "/hero.png",
         "datePublished": "2026-09-16",
         "dateModified": "2026-09-16",
         "author": {"@id": URL + "#author"},
         "publisher": {"@id": "https://www.nexusguard.com/#org"},
         "mainEntityOfPage": URL,
         "keywords": "low volume DDoS attacks, sub-saturating DDoS, DDoS detection, sub-1 Gbps DDoS"},
        {"@type": "Person",
         "@id": URL + "#author",
         "name": "[AUTHOR NAME]",
         "jobTitle": "[JOB TITLE]",
         "worksFor": {"@id": "https://www.nexusguard.com/#org"}},
        {"@type": "Organization",
         "@id": "https://www.nexusguard.com/#org",
         "name": "Nexusguard",
         "url": "https://www.nexusguard.com/",
         "logo": {"@type": "ImageObject", "url": "https://www.nexusguard.com/logo.png"}},
        {"@type": "BreadcrumbList",
         "@id": URL + "#breadcrumb",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.nexusguard.com/"},
             {"@type": "ListItem", "position": 2, "name": "Blog", "item": "https://www.nexusguard.com/blog"},
             {"@type": "ListItem", "position": 3, "name": "Sub-1 Gbps Attacks", "item": URL}]},
        {"@type": "FAQPage",
         "@id": URL + "#faq",
         "mainEntity": [{"@type": "Question", "name": q.strip(),
                         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', a).strip()}}
                        for q, a in faqs]},
    ],
}
block = '<script type="application/ld+json">\n' + json.dumps(graph, indent=2) + '\n</script>\n'
html = re.sub(r'<script type="application/ld\+json">.*?</script>\n', block, html, count=1, flags=re.S)
pathlib.Path(SLUG + ".html").write_text(html)
print(f"schema graph injected ({len(faqs)} FAQ entities)")
