# Enna

An oil sprayer designed for Indian kitchens. This repository holds the product
research, the design and manufacturing brief, and the marketing site.

```
docs/    research, product brief, strategy, manufacturing and BOM
site/    the marketing site — deployed as-is to AWS Amplify
scripts/ build-artifact.mjs — generates the Claude Artifact variant
build/   generated; not the deploy target
```

## The site

`site/index.html` is a single self-contained page. It has no build step and no
dependencies beyond two CDN loads (Google Fonts and Three.js). The exploded
product view is generated procedurally in Three.js — there are no model files
to fetch.

### Deploying to AWS Amplify

1. In the Amplify console choose **Host web app** → **GitHub**, and authorise
   the repository.
2. Pick the branch you want to deploy.
3. Amplify will detect `amplify.yml` at the repository root. It publishes
   `site/` as-is with no build command, so no framework preset is needed.
4. Deploy. Amplify serves the app on an `amplifyapp.com` subdomain immediately.
5. For a custom domain, go to **Hosting → Custom domains** and follow the
   verification steps. Amplify provisions the TLS certificate automatically.

`site/customHttp.yml` sets security headers and cache policy. Amplify reads it
from the root of the published directory, which is why it lives in `site/`
rather than the repository root.

To deploy from the CLI instead:

```bash
npm install -g @aws-amplify/cli
amplify configure          # one-time, sets up your IAM user
amplify init
amplify add hosting
amplify publish
```

### Local preview

```bash
npx http-server site -p 8080
```

### Regenerating the Artifact variant

The Claude Artifact host supplies its own document skeleton, so it needs a
body-only version of the page. One source of truth, two targets:

```bash
node scripts/build-artifact.mjs   # writes build/artifact.html
```

Run this after any change to `site/index.html`.

## Status

Enna is a design concept with a costed path to production. Every specification
in `docs/` and on the site is a design target, not a measured production value.
