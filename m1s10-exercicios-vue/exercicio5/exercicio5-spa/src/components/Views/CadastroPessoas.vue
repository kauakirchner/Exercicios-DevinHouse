<template>
  <div class="container">
      <router-view></router-view>
      <h1>Estamos no componente de cadastro de pessoas!</h1>
      <div class="form">
          <form>
            <div class="row">
                <div>
                <input type="text" placeholder="Nome" class="form-control" v-model="pessoa.nome">
                <hr>
                </div>               
                <div>
                <input type="email" placeholder="Email" class="form-control" v-model="pessoa.email"> 
                <hr>
                </div>               
                <div>
                <input type="number" placeholder="Idade" class="form-control" v-model="pessoa.idade"> 
                </div>                
            </div>
          </form>
          <div class="col-2">
             <div class="col-2">
                <button type="button" class="btn btn-primary" @click="cadastraPessoa">Enviar</button>
            </div>            
          </div>
      </div>
  </div>
</template>

<script>
export default {
       data(){
        return{
           pessoas:[],
           pessoa:{
               nome: null,
               idade: null,
               id: null,
               email: null
           } 
        }
    },

    methods:{
        getPessoas(){
            return this.$store.state.pessoas
        },
        cadastraPessoa(){
            this.$store.commit('cadastraPessoa',{
                "id": new Date().getTime(),
                "nome": this.pessoa.nome,
                "idade": this.pessoa.idade,
                "email": this.pessoa.email
            })
            this.$router.push('/listagem')
            this.pessoa = {}
        }
    }
}
</script>

<style>

</style>