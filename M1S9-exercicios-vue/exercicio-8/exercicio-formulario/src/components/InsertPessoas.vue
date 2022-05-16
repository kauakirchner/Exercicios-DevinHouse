<template>
  <div class="container">
      <div class="Form">
        <form>
            <input type="text" placeholder="Nome" class="form-control" v-model="pessoa.nome">
            <hr>
            <input type="number" placeholder="Idade" class="form-control" v-model="pessoa.idade">
        </form>
        <hr>
        <button type="button" class="btn btn-primary" @click="insertPessoa">Inserir</button>
        <hr>
      </div>
      <div class="row">
          <table>
              <thead>
                <tr>
                <th class="col-1">Nome</th>
                <th class="col-1">Idade</th>
                </tr>
              </thead>
              <tbody>
                  <tr v-for="i in pessoas" :key="i">
                    <td v-text="pessoa.nome"></td>
                    <td v-text="pessoa.idade"></td>
                  </tr>
              </tbody>
          </table>
      </div>
  </div>
</template>

<script>
export default {
    name: 'InsertPessoa',
    data(){
        return{
            pessoas:[],
            pessoa:{}
        }
    },
    methods:{
        insertPessoa(){
            this.pessoas.push(this.pessoa)
        }
    }
}
</script>

<style>

</style>