"""Screenshots (3 viewports + dark) and PDF via the pre-installed Chromium."""
import pathlib
from patchright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
SLUG = "low-volume-ddos-attacks-sub-1-gbps"
url = pathlib.Path(SLUG + ".html").resolve().as_uri()
pathlib.Path("preview").mkdir(exist_ok=True)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    for w, h in [(375, 812), (768, 1024), (1280, 800)]:
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.goto(url); pg.wait_for_timeout(400)
        pg.screenshot(path=f"preview/{w}.png", full_page=True); pg.close()
    pg = b.new_page(viewport={"width": 1280, "height": 800}, color_scheme="dark")
    pg.goto(url); pg.wait_for_timeout(400)
    dark = pg.evaluate("getComputedStyle(document.body).backgroundColor")
    pg.screenshot(path="preview/1280-dark.png", full_page=True); pg.close()
    pg = b.new_page(viewport={"width": 1280, "height": 800})
    pg.goto(url); pg.wait_for_timeout(400)
    light = pg.evaluate("getComputedStyle(document.body).backgroundColor")
    svgs = pg.evaluate("document.querySelectorAll('svg').length")
    pg.pdf(path=SLUG + ".pdf", format="A4", print_background=True); pg.close(); b.close()
print(f"live svg nodes: {svgs} | light {light} dark {dark} | console errors: {errs or 'none'}")
