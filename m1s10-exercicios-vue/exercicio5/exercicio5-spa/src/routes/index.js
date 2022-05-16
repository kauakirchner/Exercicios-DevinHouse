import {createRouter, createWebHashHistory} from 'vue-router'
import HomeA from './../components/Views/HomeA.vue'
import CadastroPessoas from './../components/Views/CadastroPessoas.vue'
import ListagemPessoas from './../components/Views/ListagemPessoas.vue'

const routes = [
    {path: '/', component: HomeA},
    {path: '/cadastro', component: CadastroPessoas},
    {path:'/listagem', component: ListagemPessoas}
]

const router = createRouter({
    routes,
    history: createWebHashHistory()
})

export default router