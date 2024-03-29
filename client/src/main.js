import { createApp } from 'vue'
import router from './router'
import './style.css'
import 'primeicons/primeicons.css'
import App from './App.vue'
import './axios'
import { createPinia } from 'pinia'

createApp(App)
    .use(createPinia())
    .use(router)
    .mount('#app')
