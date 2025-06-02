import { Hono } from 'hono'
import { serveStatic } from 'hono/cloudflare-workers'

const app = new Hono()

// Serve static assets from ./public
app.use('/*', serveStatic({ root: './public' }))

// Example API endpoint
app.post('/api/chat', async (c) => {
  const { message, history } = await c.req.json()
  // ...OpenAI API logic here
  return c.json({ reply: "This is a placeholder reply from Sigfrid von Shrink." })
})

export default app
