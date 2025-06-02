import { serveStatic } from "@hono/node-server/serve-static";
import { Hono } from "hono";

const app = new Hono();

// Serve static assets from public
app.use("/*", serveStatic({ root: "./public" }));

// Example API endpoint (migrated from /functions/api/chat.js)
app.post("/api/chat", async (c) => {
  const { message, history } = await c.req.json();
  // ...OpenAI API logic here (use env vars)
  return c.json({ reply: "This is a placeholder reply from Sigfrid von Shrink." });
});

export default app;
