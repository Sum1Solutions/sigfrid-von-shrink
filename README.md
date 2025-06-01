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
- **Memory:** Conversation memory is managed client-side (in the browser) and sent with each request.
- **Deployment:** GitHub integration, automatic deploys, environment variables set in Cloudflare dashboard.
- **No Python required:** Fully serverless, modern, and scalable.

### Why the Change?
- **Performance:** Serverless functions scale instantly, no cold starts or server maintenance.
- **Simplicity:** No Python or Flask dependencies—just JavaScript and static files.
- **Security:** API keys and secrets managed via Cloudflare dashboard, never in code.
- **Modern best practices:** GitHub-based CI/CD, instant rollbacks, and preview deploys.
- **Cost:** Free/low-cost hosting for static and serverless apps.

---

## Quick Start (Local Dev)

1. Clone the repository:
   ```sh
   git clone https://github.com/Sum1Solutions/Sigfrid-von-Shrink.git
   cd Sigfrid-von-Shrink
   ```
2. Install Wrangler CLI (if not already):
   ```sh
   npm install -g wrangler
   ```
3. Add your OpenAI key and config to `.dev.vars` (never commit this file!):
   ```env
   OPENAI_API_KEY=sk-...
   OPENAI_MODEL=gpt-3.5-turbo
   OPENAI_TEMPERATURE=0.7
   OPENAI_MAX_TOKENS=512
   SYSTEM_PROMPT=You are Sigfrid von Shrink, ...
   ```
4. Run locally:
   ```sh
   wrangler pages dev public
   ```
5. Open [http://localhost:8788](http://localhost:8788) and chat!

---

## Cloudflare Pages Deployment

1. **Connect GitHub repo** in Cloudflare Pages dashboard.
2. **Set build output directory:** `public`
3. **Set functions directory:** `functions`
4. **Add environment variables** (OPENAI_API_KEY as secret, others as text).
5. **Push to GitHub**: Deploys are automatic.
6. **Access your app:** e.g., `https://sigfrid-von-shrink.pages.dev` or your custom domain.

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

---
