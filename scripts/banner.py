"""Regenerates the animated profile banner (dark + light) with live GitHub data."""
import json, os, urllib.request, html

USER = "rafeyshah"
SKIP = {USER}

def latest_repo():
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=20&type=owner",
        headers={"Accept": "application/vnd.github+json",
                 **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})})
    try:
        repos = json.load(urllib.request.urlopen(req, timeout=20))
        for r in repos:
            if not r["fork"] and not r["private"] and r["name"] not in SKIP:
                name = r["name"].split("-")[0] if len(r["name"]) > 22 else r["name"]
                return name[:22]
    except Exception as e:
        print("API error:", e)
    return "GawainBook"

F = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
M = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, 'Liberation Mono', monospace"

def svg(dark, repo):
    if dark:
        bg1, bg2, fg, mute, grid = "#0D1117", "#0B1220", "#E6EDF3", "#8B949E", "#30363D"
        card, cardb, chipbg = "#161B22", "#30363D", "#161B22"
        gA, gB, key, prop, strc, pun = "#1F6FEB", "#2EA44F", "#FF7B72", "#79C0FF", "#A5D6FF", "#8B949E"
        oA, oB, dot = 0.28, 0.18, 0.55
    else:
        bg1, bg2, fg, mute, grid = "#FFFFFF", "#F6F8FA", "#1F2328", "#59636E", "#D1D9E0"
        card, cardb, chipbg = "#FFFFFF", "#D1D9E0", "#F6F8FA"
        gA, gB, key, prop, strc, pun = "#0969DA", "#1A7F37", "#CF222E", "#0550AE", "#0A3069", "#59636E"
        oA, oB, dot = 0.12, 0.08, 0.7
    e = lambda s: html.escape(s, quote=False)

    chips = ["TypeScript", "React", "Node.js", "PostgreSQL", "PyTorch"]
    x = 64; chip_svg = ""
    for i, c in enumerate(chips):
        w = int(len(c) * 8.6 + 28)
        chip_svg += (f'<g class="up" style="animation-delay:{0.45 + i*0.08:.2f}s">'
                     f'<rect x="{x}" y="236" width="{w}" height="30" rx="15" fill="{chipbg}" stroke="{cardb}"/>'
                     f'<text x="{x + w/2}" y="256" text-anchor="middle" font-family="{F}" font-size="14" font-weight="500" fill="{fg}">{c}</text></g>')
        x += w + 10

    code = [
        [(key, "const "), (prop, "rafey"), (pun, " = {")],
        [(prop, "  builds"), (pun, ": "), (strc, '"full-stack TS products"'), (pun, ",")],
        [(prop, "  trains"), (pun, ": "), (strc, '"PyTorch models"'), (pun, ",")],
        [(prop, "  shipping"), (pun, ": "), (strc, f'"{repo}"'), (pun, ",")],
        [(prop, "  status"), (pun, ": "), (strc, '"open to work"')],
        [(pun, "};")],
    ]
    clips, lines = "", ""
    t = 0.9  # typing start
    for i, line in enumerate(code):
        y = 124 + i * 24
        chars = sum(len(s) for _, s in line)
        dur = max(0.15, chars * 0.028)
        clips += (f'<clipPath id="c{i}"><rect x="780" y="{y-17}" height="24" width="0">'
                  f'<animate attributeName="width" from="0" to="{chars*9.2+12:.0f}" begin="{t:.2f}s" dur="{dur:.2f}s" fill="freeze"/>'
                  f'</rect></clipPath>')
        spans = "".join(f'<tspan fill="{c}">{e(s)}</tspan>' for c, s in line)
        lines += f'<text x="788" y="{y}" font-family="{M}" font-size="15" xml:space="preserve" clip-path="url(#c{i})">{spans}</text>'
        t += dur + 0.12
    done = t

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-label="Abdul Rafey — Full-Stack Engineer, MSc Data Science at FAU. Open to work, Nuremberg.">
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
<radialGradient id="g1" cx="0.85" cy="0.1" r="0.55"><stop offset="0" stop-color="{gA}" stop-opacity="{oA}"/><stop offset="1" stop-color="{gA}" stop-opacity="0"/>
<animate attributeName="cx" values="0.85;0.70;0.85" dur="14s" repeatCount="indefinite"/></radialGradient>
<radialGradient id="g2" cx="0.05" cy="1" r="0.5"><stop offset="0" stop-color="{gB}" stop-opacity="{oB}"/><stop offset="1" stop-color="{gB}" stop-opacity="0"/>
<animate attributeName="cx" values="0.05;0.20;0.05" dur="18s" repeatCount="indefinite"/></radialGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{grid}" fill-opacity="{dot}"/></pattern>
<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{gB}"/><stop offset="1" stop-color="{gA}"/></linearGradient>
<clipPath id="clip"><rect width="1200" height="320" rx="16"/></clipPath>
{clips}
<style>
.up{{opacity:0;animation:up .6s cubic-bezier(.2,.7,.2,1) forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}
.pulse{{transform-box:fill-box;transform-origin:center;animation:p 2.4s ease-out infinite}}
@keyframes p{{0%{{opacity:.5;transform:scale(1)}}100%{{opacity:0;transform:scale(2.6)}}}}
.cur{{opacity:0;animation:b 1.1s steps(1) {done:.2f}s infinite}}
@keyframes b{{0%{{opacity:1}}50%{{opacity:0}}}}
.bar{{transform-origin:0 0;transform:scaleX(0);animation:grow 1.2s cubic-bezier(.2,.7,.2,1) .1s forwards}}
@keyframes grow{{to{{transform:scaleX(1)}}}}
</style>
</defs>
<g clip-path="url(#clip)">
<rect width="1200" height="320" fill="url(#bg)"/>
<rect width="1200" height="320" fill="url(#dots)"/>
<rect width="1200" height="320" fill="url(#g1)"/>
<rect width="1200" height="320" fill="url(#g2)"/>
<rect class="bar" x="0" y="0" width="1200" height="4" fill="url(#bar)"/>
</g>
<rect x="0.5" y="0.5" width="1199" height="319" rx="16" fill="none" stroke="{cardb}"/>
<g class="up" style="animation-delay:.05s">
<rect x="64" y="34" width="236" height="32" rx="16" fill="{chipbg}" stroke="{cardb}"/>
<circle class="pulse" cx="86" cy="50" r="5" fill="{gB}"/>
<circle cx="86" cy="50" r="5" fill="{gB}"/>
<text x="100" y="55" font-family="{F}" font-size="14" font-weight="500" fill="{mute}"><tspan fill="{fg}">Open to work</tspan> · Nuremberg, DE</text>
</g>
<text class="up" style="animation-delay:.15s" x="62" y="148" font-family="{F}" font-size="68" font-weight="700" letter-spacing="-1.5" fill="{fg}">Abdul Rafey</text>
<text class="up" style="animation-delay:.28s" x="64" y="194" font-family="{F}" font-size="24" font-weight="400" fill="{mute}"><tspan fill="{fg}" font-weight="600">Full-Stack Engineer</tspan>  ·  MSc Data Science @ FAU</text>
{chip_svg}
<g class="up" style="animation-delay:.5s">
<rect x="760" y="56" width="384" height="216" rx="12" fill="{card}" stroke="{cardb}"/>
<circle cx="784" cy="80" r="5.5" fill="#FF5F57"/><circle cx="802" cy="80" r="5.5" fill="#FEBC2E"/><circle cx="820" cy="80" r="5.5" fill="#28C840"/>
<text x="1120" y="85" text-anchor="end" font-family="{M}" font-size="12" fill="{mute}">about.ts</text>
<line x1="760" y1="98" x2="1144" y2="98" stroke="{cardb}"/>
</g>
{lines}
<rect class="cur" x="808" y="232" width="9" height="18" fill="{gA}"/>
</svg>'''

if __name__ == "__main__":
    repo = latest_repo()
    print("shipping:", repo)
    os.makedirs("assets", exist_ok=True)
    for name, dark in (("dark", True), ("light", False)):
        with open(f"assets/banner-{name}.svg", "w", encoding="utf-8") as f:
            f.write(svg(dark, repo))
