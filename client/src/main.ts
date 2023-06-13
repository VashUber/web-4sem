import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config'
import ToastService from 'primevue/toastservice'

import 'primevue/resources/themes/lara-light-indigo/theme.css'
import 'primevue/resources/primevue.min.css'
import './assets/main.scss'
import 'primeicons/primeicons.css'
import { fetchUser } from './utils/api/Auth'

const setup = async () => {
  await Promise.all([fetchUser()])

  const app = createApp(App)

  app.use(router)
  app.use(PrimeVue)
  app.use(ToastService)
  app.mount('#app')
}

setup()
