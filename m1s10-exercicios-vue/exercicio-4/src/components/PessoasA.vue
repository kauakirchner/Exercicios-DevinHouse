<template>
  <div class="container">
    <div class="form">
      <form>
        <input type="text" placeholder="Nome" class="form-control" v-model="pessoa.nome">
        <hr>
        <input type="number" placeholder="Idade" class="form-control" v-model="pessoa.idade">
        <hr>
        </form>
        <hr>
        <div class="col-2">
          <button type="button"  @click="adicionaPessoas" class="btn btn-primary" @keypress="enter">Cadastrar</button>
        </div>
      <table v-if="this.$store.state.pessoas.length > 0">
        <thead>
          <tr>
            <th class="col-3">Nome</th>   
            <th class="col-3">Idade</th> 
          </tr>
        </thead>   
          <transition-group name="pessoas" tag="tbody"> 
            <tr v-for="(i, index) in this.$store.state.pessoas" :key="index">
              <td>{{i.nome}}</td>   
              <td>{{i.idade}}</td>
              <button type="button" @click="deletaItem(index)" class="btn btn-danger">Deletar item</button>
              <hr>
            </tr>
            </transition-group>        
      </table>
      <div v-else>
        <h1>Não há pessoas cadastradas!!</h1> 
      </div>
    </div>
  </div>
</template>
<script>
export default {
    name: 'PessoasA',

    data(){
      return{
        pessoas:[],
        pessoa:{
          id: '',
          nome: null,
          idade:''
        }
      }
    },
    methods:{
      adicionaPessoas(){
        this.$store.commit('adicionaPessoas',{
          "id": new Date().getTime(),
          "nome": this.pessoa.nome,
          "idade": this.pessoa.idade
        })
        this.pessoa = {}
      },

      getPessoas(){
        return this.$store.state.pessoas
      },
      deletaItem(index){
        this.$store.commit('deletaItem', index)
      },
  }
}
</script>

<style>
.pessoas-leave-to,
.pessoas-enter-from{
  opacity: 0;
  font-size: 0px;
}
.pessoas-leave-from,
.pessoas-enter-to{
  opacity: 1;
  font-size: 2.5rem;
}
.pessoas-move,
.pessoas-enter-active,
.pessoas-leave-active{
  transition:all 2s;
}
</style>