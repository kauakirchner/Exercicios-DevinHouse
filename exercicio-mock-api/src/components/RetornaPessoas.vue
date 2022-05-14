<template>
  <div class="container">
      <div class="row">
                <div v-if="users.length === 0">
          Sem usuarios cadastrados
      </div>
      <table v-else>
          <thead>
              <tr>
                  <th class="col-3">Id</th>                 
                  <th class="col-3">Nome</th>                 
                  <th>Idade</th>
                  <th>Email</th>                 
              </tr>
          </thead>
          <tbody>
              <tr v-for="user in users" :key="user.id">
                  <td v-text="user.id" class="col-3"></td>                 
                  <td v-text="user.nome" class="col-3"></td>                 
                  <td v-text="user.idade" class="col-3"></td>
                   <td v-text="user.email" class="col-3"></td>
              </tr>
          </tbody>
      </table>
      </div>
  </div>
</template>

<script>
export default {
   mounted(){
        this.$store.dispatch('module2/load')
    },
    computed:{
        users(){
            return this.$store.state.module2.users
        }
    }
}
</script>

<style>

</style>