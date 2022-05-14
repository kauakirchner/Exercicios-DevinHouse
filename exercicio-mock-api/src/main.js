import { createApp } from 'vue'
import App from './App.vue'
import {createRouter, createWebHashHistory} from 'vue-router';
import MockApi from './components/MockApi.vue'
import RetornaPessoas from './components/RetornaPessoas.vue'
import store from './store';
import NhomeA from './components/NhomeA.vue'



 

const routes = [
    {path:'/home', component: NhomeA},
    {path: '/mock', component: MockApi,},
    {path: '/retorna', component: RetornaPessoas},
]

const router = createRouter({
    routes,
    history: createWebHashHistory(),

})


const app = createApp(App); 
app.use(store);
app.use(router);
app.mount('#app');