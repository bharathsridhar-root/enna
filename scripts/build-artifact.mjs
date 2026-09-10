/* Generates build/artifact.html — the body-only variant the Claude Artifact
   host expects — from the standalone site/index.html that Amplify deploys.
   One source of truth, two targets. */
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';

const src = readFileSync(new URL('../site/index.html', import.meta.url), 'utf8');

const head = src.match(/<head[^>]*>([\s\S]*?)<\/head>/i)?.[1];
const body = src.match(/<body[^>]*>([\s\S]*?)<\/body>/i)?.[1];
if (!head || !body) throw new Error('site/index.html: could not find <head> or <body>');

// The artifact skeleton supplies charset, viewport and a reset; everything else
// in <head> (title, font link, styles) has to travel with the page.
const carried = head
  .split('\n')
  .filter((l) => !/<meta\s+(charset|name="viewport"|name="theme-color"|property="og:|name="description")/i.test(l))
  .join('\n')
  .trim();

mkdirSync(new URL('../build/', import.meta.url), { recursive: true });
writeFileSync(new URL('../build/artifact.html', import.meta.url), `${carried}\n${body.trim()}\n`);
console.log('wrote build/artifact.html');
