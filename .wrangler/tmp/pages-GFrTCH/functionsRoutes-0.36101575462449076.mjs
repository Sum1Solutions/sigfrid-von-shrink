import { onRequestPost as __api_chat_js_onRequestPost } from "/Users/jb/coding/Sigfrid-von-Shrink/functions/api/chat.js"

export const routes = [
    {
      routePath: "/api/chat",
      mountPath: "/api",
      method: "POST",
      middlewares: [],
      modules: [__api_chat_js_onRequestPost],
    },
  ]