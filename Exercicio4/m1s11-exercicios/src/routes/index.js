import {createRouter, createWebHashHistory} from  'vue-router'
import HomeA from './components/HomeA.vue'
import InserePessoa from './components/InserePessoa.vue'

const routes = [
    {path: '/', component: HomeA},
    {path: '/insert', component: InserePessoa}
]

const router = createRouter({
    routes,
    history: createWebHashHistory()
})

export default router