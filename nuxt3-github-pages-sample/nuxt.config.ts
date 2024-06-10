// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  devtools: { enabled: true },
  app: {
    baseURL: "/repository-name/",
    head: {
      link: [{ rel: "icon", type: "image/png", href: "/repository-name/favicon.png" }],
    },
  },
});
