<template>
  <div>
    <HeaderComponent />
    <Nuxt-Page />
    <FooterComponent />
  </div>
</template>

<script>
import HeaderComponent from '~/components/Header.vue'
import FooterComponent from '~/components/Footer.vue'

export default {
  components: {
    HeaderComponent,
    FooterComponent,
  }
}
</script>

<script setup>
useHead({
  title: 'web title',
  meta: [
    { charset: 'utf-8' },
    { 'http-equiv': 'X-UA-Compatible', content: 'IE=edge' },
    { name: 'viewport', content: 'width=device-width,initial-scale=1.0' },
    { name: 'description', content: '{{description text}}' },
    { name: 'author', content: 'web title' },
    { property: 'og:title', content: 'web title' },
    { property: 'og:type', content: 'website' },
    { property: 'og:description', content: '{{description text}}' },
    { property: 'og:site_name', content: 'web title' },
    { name: 'google-site-verification', content: 'your-verification-code' }, // Add your verification code here
  ],
  link: [
    { rel: 'preconnect', href: 'https://fonts.googleapis.com' },
    { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true },
    {
      href: 'https://fonts.googleapis.com/css2?family=Klee+One&family=Noto+Sans+JP:wght@300&display=swap',
      rel: 'stylesheet',
    },
  ],
})
</script>

<style lang="scss">
html {
  padding: 0;
  margin: 0;

  body {
    padding: 0;
    margin: 0;
  }
}
</style>