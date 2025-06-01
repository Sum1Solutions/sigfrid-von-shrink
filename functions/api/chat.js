export async function onRequestPost(context) {
  const { request, env } = context;
  const { message, history } = await request.json();

  let messages = [];
  if (env.SYSTEM_PROMPT) {
    messages.push({ role: 'system', content: env.SYSTEM_PROMPT });
  }
  if (Array.isArray(history)) {
    for (const turn of history) {
      messages.push({ role: turn.role, content: turn.content });
    }
  } else if (message) {
    messages.push({ role: 'user', content: message });
  }

  const apiKey = env.OPENAI_API_KEY;
  const model = env.OPENAI_MODEL || 'gpt-3.5-turbo';
  const temperature = env.OPENAI_TEMPERATURE ? parseFloat(env.OPENAI_TEMPERATURE) : 0.7;
  const max_tokens = env.OPENAI_MAX_TOKENS ? parseInt(env.OPENAI_MAX_TOKENS) : 512;

  try {
    const openaiRes = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model,
        messages,
        temperature,
        max_tokens,
      }),
    });

    if (!openaiRes.ok) {
      const error = await openaiRes.text();
      return new Response(JSON.stringify({ error }), { status: 500, headers: { 'Content-Type': 'application/json' } });
    }

    const data = await openaiRes.json();
    const aiMessage = data.choices[0].message.content.trim();

    return new Response(JSON.stringify({ message: aiMessage }), {
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}

