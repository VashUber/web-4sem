import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000,
    strictPort: true,
    host: true
  },

  css: {
    preprocessorOptions: {
      scss: {
        additionalData: `
          @import "@/assets/variables.scss";
        `
      }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      'ui-components': fileURLToPath(new URL('./src/uiComponents.ts', import.meta.url))
    }
  }
})
