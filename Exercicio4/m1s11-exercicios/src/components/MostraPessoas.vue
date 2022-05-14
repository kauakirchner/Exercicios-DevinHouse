<template>
  <div class="container">
      <h1>Pessoas Cadastradas:</h1>
      <hr>
      <div>
          <table>
              <thead>
                  <tr>
                      <th class="col-3">Id</th>
                      <th class="col-3">Nome</th>                 
                      <th class="col-3">Idade</th>                    
                      <th class="col-3">Email</th>                   
                  </tr>
              </thead>
              <tbody>
                  <tr v-for="user in users" :key="user.Id">
                    <td v-text="user.id"></td>
                    <td v-text="user.nome"></td>
                    <td v-text="user.idade"></td>
                    <td v-text="user.email"></td>
                  </tr>
              </tbody>
          </table>
      </div>
  </div>
</template>

<script>
export default {
   mounted(){
        this.$store.dispatch('moduloLoad/load')
    },
    computed:{
        users(){
            return this.$store.state.moduloLoad.users
        }
    }
}
</script>

<style>

</style>