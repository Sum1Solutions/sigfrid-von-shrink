# Sigfrid von Shrink

Sigfrid von Shrink is a chatbot inspired by the AI psychoanalyst in Frederik Pohl's science fiction novel [Gateway](https://en.wikipedia.org/wiki/Gateway_(novel)) (the first in the Heechee Saga). Sigfrid is powered by OpenAI's ChatGPT. (Satirical, not medical advice!)

---

## Project Evolution: Python/Flask → Cloudflare Pages/Workers (2025+)

### Legacy Approach (2023)
- **Backend:** Python Flask app, session memory, Flask-Session, OpenAI Python SDK.
- **Frontend:** Jinja2 HTML templates, static JS/CSS, Flask routes.
- **Deployment:** Manual or Heroku-style, Python dependencies, `.env` files.

### Modern Approach (2025+)
- **Backend:** Cloudflare Pages + Cloudflare Functions (JavaScript/Node.js, serverless).
- **Frontend:** Static assets in `/public` (HTML, CSS, JS, images).
- **API:** `/functions/api/chat.js` handles chat via OpenAI API using native `fetch` (no SDKs).
---

## Overview
- **Platform:** Cloudflare Workers (edge, serverless)
- **Features:**
  - Static site (chat UI, assets) served from `/public`
  - Serverless API endpoint at `/api/chat` (OpenAI integration)
  - Secure environment variables
  - No servers, no DevOps, instant global scaling

## Architecture
- **worker.js:** Main Worker script (serves static + API)
- **public/**: Static assets (HTML, CSS, JS, images)
- **wrangler.toml:** Worker/project config

## Directory Structure
```
/
├── public/
│   ├── index.html
│   ├── css/
│   ├── images/
│   └── js/
├── worker.js
├── wrangler.toml
├── package.json
└── README.md
```

## Local Development
1. Clone the repo:
   ```sh
   git clone https://github.com/Sum1Solutions/Sigfrid-von-Shrink.git
   cd Sigfrid-von-Shrink
   ```
2. Install dependencies:
   ```sh
   npm install hono @hono/node-server
   ```
3. Add your OpenAI key and config to `.dev.vars` (never commit this file!):
   ```env
   OPENAI_API_KEY=sk-...
   OPENAI_MODEL=gpt-3.5-turbo
   OPENAI_TEMPERATURE=0.7
   OPENAI_MAX_TOKENS=512
   SYSTEM_PROMPT=You are Sigfrid von Shrink, ...
   ```
4. Start local dev:
   ```sh
   npx wrangler dev
   ```
5. Open [http://localhost:8787](http://localhost:8787) and chat!

## Deploy to Cloudflare Workers
1. Set environment variables in the Cloudflare dashboard (Secrets).
2. Deploy:
   ```sh
   npx wrangler deploy
   ```
3. Access your app at your Workers domain or custom domain.

## How Static + API Routing Works
- **Static assets:** Any request matching a file in `/public` is served as static.
- **API endpoint:** POST `/api/chat` is handled by the Worker (calls OpenAI, returns reply).
- **All other routes:** Fallback to static or 404.

## Environment Variables
- Set in `.dev.vars` for local dev (never commit!)
- Set in Cloudflare dashboard for production

## Why Cloudflare Workers?
- Unified static + dynamic at the edge
- No servers, instant scaling
- Generous free tier
- Modern, future-proof architecture

---

> This repo is an example of best practices for deploying modern web apps on Cloudflare Workers. Fork, adapt, and build your own edge-powered projects!

---

## Contributing
Issues and PRs are welcome! See [GitHub repo](https://github.com/Sum1Solutions/Sigfrid-von-Shrink).

## License
MIT License.

---

### Historical Note
This project began as a Flask/Python experiment but is now a modern, serverless, scalable Cloudflare Pages/Workers app. All legacy backend code has been removed for clarity and maintainability.
3. **Build Output Directory**: Set to `public`.
4. **Functions Directory**: Set to `functions` (auto-detected).

### Environment Variables (Secrets)
- Go to your Cloudflare Pages project > Settings > Environment Variables.
- Add:
  - `OPENAI_API_KEY` — your OpenAI API key
  - `OPENAI_MODEL` (optional, default: `gpt-3.5-turbo`)
  - `OPENAI_TEMPERATURE` (optional, e.g. `0.7`)
  - `OPENAI_MAX_TOKENS` (optional, e.g. `512`)
  - `SYSTEM_PROMPT` (optional, system message for the AI)

### How the Chat API Works
- The frontend sends a POST request to `/api/chat` with `{ message, history }`.
- The Cloudflare Function builds the prompt and calls OpenAI, returning the AI response.
- Conversation memory can be managed in the browser (localStorage) for stateless memory, or sent as `history` with each request.

### Local Development
- Install [Wrangler CLI](https://developers.cloudflare.com/pages/platform/functions/#developing-functions-locally) for local testing:
  ```sh
  npm install -g wrangler
  wrangler pages dev public
  ```
- Or push to GitHub and let Cloudflare Pages deploy automatically.

### Project Structure (Cloudflare Pages)
```
/public            # Static site assets (index.html, css, js, images)
/functions/api/    # Cloudflare Functions (chat.js)
package.json       # Node.js dependencies for Functions
```


This project is licensed under the MIT License given that I don't really understand all the options and what they mean.

---

## Cloudflare Pages Deployment (2025+)

### Overview
- **Frontend**: All static files are in `/public` (HTML, CSS, JS, images).
- **API Backend**: `/functions/api/chat.js` is a Cloudflare Function (using Node.js) that handles chat requests and calls OpenAI.
- **No Python required**: All backend logic is now serverless JavaScript.

### Automatic Deploys from GitHub
1. **Push to GitHub**: Any push to your repo triggers a new build on Cloudflare Pages.
2. **Cloudflare Pages**: Connect your GitHub repo in the Cloudflare Pages dashboard.
3. **Build Output Directory**: Set to `public`.
4. **Functions Directory**: Set to `functions` (auto-detected).

### Environment Variables (Secrets)
- Go to your Cloudflare Pages project > Settings > Environment Variables.
- Add:
  - `OPENAI_API_KEY` — your OpenAI API key
  - `OPENAI_MODEL` (optional, default: `gpt-3.5-turbo`)
  - `OPENAI_TEMPERATURE` (optional, e.g. `0.7`)
  - `OPENAI_MAX_TOKENS` (optional, e.g. `512`)
  - `SYSTEM_PROMPT` (optional, system message for the AI)

### How the Chat API Works
- The frontend sends a POST request to `/api/chat` with `{ message, history }`.
- The Cloudflare Function builds the prompt and calls OpenAI, returning the AI response.
- Conversation memory can be managed in the browser (localStorage) for stateless memory, or sent as `history` with each request.

### Local Development
- Install [Wrangler CLI](https://developers.cloudflare.com/pages/platform/functions/#developing-functions-locally) for local testing:
  ```sh
  npm install -g wrangler
  wrangler pages dev public
  ```
- Or push to GitHub and let Cloudflare Pages deploy automatically.

### Project Structure (Cloudflare Pages)
```
/public            # Static site assets (index.html, css, js, images)
/functions/api/    # Cloudflare Functions (chat.js)
package.json       # Node.js dependencies for Functions
```

---
