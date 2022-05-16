<template>
  <div class="container">
    <div class="form">
      <table v-if="this.$store.state.pessoas.length > 0">
        <thead>
          <tr>
            <th class="col-3">Nome</th>   
            <th class="col-3">Idade</th> 
          </tr>
        </thead>   
          <tbody> 
            <tr v-for="(i, index) in this.$store.state.pessoas" :key="index">
              <td>{{i.nome}}</td>   
              <td>{{i.idade}}</td>
              <button type="button" @click="deletaPessoa(index)" class="btn btn-danger">Deletar item</button>
              <hr>
            </tr>
          </tbody>        
      </table>
      <div v-else>
        <h1>Não há pessoas cadastradas!!</h1> 
      </div>
    </div>
  </div>
</template>

<script>
export default {
    data(){
        return{
            pessoas:[],
            pessoa:{}
        }
    },
  methods:{
       getPessoas(){
            return this.$store.state.pessoas
        },
        deletaPessoa(index){
            this.$store.commit('deletaPessoa', index)
        }
  }
}
</script>

<style>

</style>