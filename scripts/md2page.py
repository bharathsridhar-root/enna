#!/usr/bin/env python3
"""Render a markdown document into a standalone styled page, so the patent draft
has one source of truth: docs/09-patent.md."""
import re, sys, html

def inline(t):
    t = html.escape(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])', r'<em>\1</em>', t)
    return t

def convert(md):
    out, i, lines = [], 0, md.split('\n')
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            i += 1; buf = []
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(html.escape(lines[i])); i += 1
            out.append('<pre><code>' + '\n'.join(buf) + '</code></pre>'); i += 1; continue
        if re.match(r'^\s*---\s*$', l):
            out.append('<hr>'); i += 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', l)
        if m:
            lv = len(m.group(1))
            txt = inline(m.group(2))
            anchor = re.sub(r'[^a-z0-9]+', '-', m.group(2).lower()).strip('-')[:40]
            out.append(f'<h{lv} id="{anchor}">{txt}</h{lv}>'); i += 1; continue
        if l.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append(lines[i]); i += 1
            cells = [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            body = [r for r in cells if not all(re.fullmatch(r':?-{2,}:?', c or '-') for c in r)]
            head, rest = body[0], body[1:]
            t = ['<div class="scroll"><table><thead><tr>']
            t += [f'<th>{inline(c)}</th>' for c in head]
            t.append('</tr></thead><tbody>')
            for r in rest:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            t.append('</tbody></table></div>')
            out.append(''.join(t)); continue
        if l.startswith('> '):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i][1:].lstrip()); i += 1
            # join first, then format: bold spanning a line break must still close
            out.append('<blockquote>' + inline(' '.join(b for b in buf if b)) + '</blockquote>'); continue
        m = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', l)
        if m:
            ordered = bool(re.match(r'\d', m.group(2)))
            tag = 'ol' if ordered else 'ul'
            items = []
            while i < len(lines):
                mm = re.match(r'^(\s*)([-*]|\d+\.)\s+(.*)$', lines[i])
                if mm:
                    items.append(mm.group(3)); i += 1
                elif lines[i].startswith('  ') and lines[i].strip() and items:
                    items[-1] += ' ' + lines[i].strip(); i += 1
                else:
                    break
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>')
            continue
        if l.strip() == '':
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,4}\s|\||>\s|```|\s*[-*]\s|\s*\d+\.\s|\s*---\s*$)', lines[i]):
            buf.append(lines[i].strip()); i += 1
        out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)

md = open(sys.argv[1], encoding='utf-8').read()
title, subtitle, backlink = sys.argv[3], sys.argv[4], sys.argv[5]
body = convert(md)
# the first h1 becomes the masthead, so strip it from the flow
body = re.sub(r'^<h1[^>]*>.*?</h1>\s*', '', body, count=1, flags=re.S)
# an <hr> immediately before an <h1> doubles up with that heading's own rule
body = re.sub(r'<hr>\s*(?=<h1)', '', body)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(subtitle)}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0E1215">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@400;500&family=Instrument+Sans:wght@400;500;600&display=swap">
<style>
:root{{
  --ground:#F1F3F4; --surface:#FFFFFF; --sunk:#E9EDEE;
  --ink:#10161A; --ink-2:#47555E; --ink-3:#74838C;
  --line:#D2D9DC; --line-soft:#E2E7E9;
  --accent:#A96C12; --accent-soft:rgba(217,164,65,.14); --warn:#8A4B2A;
  --display:"Bricolage Grotesque","Trebuchet MS",system-ui,sans-serif;
  --body:"Instrument Sans","Helvetica Neue",Arial,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
  --gut:clamp(20px,5vw,56px);
}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{
  --ground:#0E1215; --surface:#161C21; --sunk:#11161A;
  --ink:#ECF1F3; --ink-2:#9DAAB3; --ink-3:#74838C;
  --line:#273038; --line-soft:#1D242A;
  --accent:#E0A63F; --accent-soft:rgba(224,166,63,.12); --warn:#D9885A;
}}}}
:root[data-theme="dark"]{{
  --ground:#0E1215; --surface:#161C21; --sunk:#11161A;
  --ink:#ECF1F3; --ink-2:#9DAAB3; --ink-3:#74838C;
  --line:#273038; --line-soft:#1D242A;
  --accent:#E0A63F; --accent-soft:rgba(224,166,63,.12); --warn:#D9885A;
}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{margin:0;background:var(--ground);color:var(--ink);font-family:var(--body);
  font-size:16px;line-height:1.72;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:860px;margin:0 auto;padding-inline:var(--gut)}}
header.mast{{border-bottom:1px solid var(--line);padding-block:clamp(38px,7vw,72px) 32px;
  margin-bottom:clamp(30px,5vw,54px)}}
.backlink{{display:inline-flex;gap:7px;font-family:var(--mono);font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;color:var(--accent);
  text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:3px}}
.kicker{{font-family:var(--mono);font-size:11px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ink-3);margin-top:24px}}
h1.big{{font-family:var(--display);font-weight:800;font-size:clamp(32px,5.2vw,56px);
  line-height:1.04;letter-spacing:-.026em;margin:14px 0 0;text-wrap:balance}}
.sub{{font-size:17px;color:var(--ink-2);max-width:60ch;margin-top:16px}}
h1,h2,h3,h4{{font-family:var(--display);font-weight:800;line-height:1.12;
  letter-spacing:-.022em;text-wrap:balance}}
h1{{font-size:clamp(27px,3.8vw,38px);margin:64px 0 0;padding-top:30px;
  border-top:1px solid var(--line)}}
h2{{font-size:clamp(21px,2.7vw,27px);margin:46px 0 0}}
h3{{font-size:18px;margin:34px 0 0}}
h4{{font-size:16px;margin:26px 0 0}}
p{{margin:15px 0 0;color:var(--ink-2);max-width:72ch}}
p strong,li strong{{color:var(--ink);font-weight:600}}
ul,ol{{margin:15px 0 0;padding-left:22px;color:var(--ink-2);max-width:72ch}}
li{{margin-bottom:9px}}
hr{{border:0;border-top:1px solid var(--line-soft);margin:44px 0 0}}
blockquote{{margin:22px 0 0;padding:18px 22px;background:var(--surface);
  border:1px solid var(--line-soft);border-left:3px solid var(--warn);
  border-radius:2px;color:var(--ink-2);font-size:15px}}
blockquote strong{{color:var(--ink)}}
code{{font-family:var(--mono);font-size:.88em;background:var(--sunk);
  padding:2px 5px;border-radius:3px;color:var(--ink)}}
pre{{margin:20px 0 0;background:var(--sunk);border:1px solid var(--line-soft);
  border-radius:3px;padding:18px 20px;overflow-x:auto}}
pre code{{background:none;padding:0;font-size:13.5px;line-height:1.6}}
.scroll{{overflow-x:auto;margin:24px 0 0}}
table{{width:100%;border-collapse:collapse;font-size:14px;min-width:520px}}
th,td{{text-align:left;padding:11px 13px;border-bottom:1px solid var(--line-soft);
  vertical-align:top}}
thead th{{font-family:var(--mono);font-size:10px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--ink-3);font-weight:400;
  border-bottom:1px solid var(--line)}}
td{{color:var(--ink-2)}} td strong{{color:var(--ink)}}
footer{{margin-top:64px;padding-block:40px;border-top:1px solid var(--line);
  font-family:var(--mono);font-size:11px;color:var(--ink-3);line-height:1.9}}
footer a{{color:var(--accent);text-decoration:none;border-bottom:1px solid var(--line)}}
@media (prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
:focus-visible{{outline:2px solid var(--accent);outline-offset:3px}}
</style>
</head>
<body>
<header class="mast"><div class="wrap">
  <a class="backlink" href="{backlink}">Back to Enna</a>
  <div class="kicker">Draft for instructing a patent attorney</div>
  <h1 class="big">{html.escape(title)}</h1>
  <p class="sub">{html.escape(subtitle)}</p>
</div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <div><a href="{backlink}">Back to Enna</a> &nbsp;·&nbsp;
    <a href="engineering.html">Engineering notes</a></div>
  <div style="margin-top:12px">Prepared 16 September 2026. Not legal advice.
    No professional novelty search has been conducted.</div>
</div></footer>
</body>
</html>'''
open(sys.argv[2], 'w', encoding='utf-8').write(page)
print('wrote', sys.argv[2], len(page), 'bytes')
