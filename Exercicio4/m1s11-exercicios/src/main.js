import { createApp } from 'vue'
import App from './App.vue'
import store from './store'
import {createRouter, createWebHashHistory} from  'vue-router'
import HomeA from './components/HomeA.vue'
import InserePessoa from './components/InserePessoa.vue'
import MostraPessoas from './components/MostraPessoas.vue'

const routes = [
    {path: '/home', component: HomeA},
    {path: '/insert', component: InserePessoa},
    {path: '/pessoas', component: MostraPessoas}
]

const router = createRouter({
    routes,
    history: createWebHashHistory()
})



const app = createApp(App); 
app.use(store);
app.use(router);
app.mount('#app');
