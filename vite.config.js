import { resolve } from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        about: resolve(__dirname, 'about.html'),
        products: resolve(__dirname, 'products.html'),
        services: resolve(__dirname, 'services.html'),
        portal: resolve(__dirname, 'portal.html'),
                privacyPolicy: resolve(__dirname, 'privacy-policy.html'),
        software: resolve(__dirname, 'software.html'),
        videoEditing: resolve(__dirname, 'video-editing.html'),
        contact: resolve(__dirname, 'contact.html'),
      },
    },
  },
})
