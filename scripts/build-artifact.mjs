/* Generates the body-only variants the Claude Artifact host expects, from the
   standalone pages Amplify deploys. One source of truth per page, two targets. */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

const PAGES = [
  { src: '../site/index.html', out: '../build/artifact.html' },
  { src: '../site/engineering.html', out: '../build/dossier.html' },
];

mkdirSync(new URL('../build/', import.meta.url), { recursive: true });

for (const { src, out } of PAGES) {
  const html = readFileSync(new URL(src, import.meta.url), 'utf8');
  const head = html.match(/<head[^>]*>([\s\S]*?)<\/head>/i)?.[1];
  const body = html.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1];
  if (!head || !body) throw new Error(`${src}: could not find <head> or <body>`);

  // The artifact skeleton supplies charset, viewport and a reset; everything
  // else in <head> (title, font link, styles) has to travel with the page.
  const carried = head
    .split('\n')
    .filter((l) => !/<meta\s+(charset|name="viewport"|name="theme-color"|name="robots"|property="og:|name="description")/i.test(l))
    .join('\n')
    .trim();

  // Relative page links do not resolve between two separate artifacts.
  const linked = body.replace(/href="(index|engineering)\.html"/g, 'href="#" data-page="$1"');

  writeFileSync(new URL(out, import.meta.url), `${carried}\n${linked.trim()}\n`);
  console.log('wrote', out.replace('../', ''));
}
