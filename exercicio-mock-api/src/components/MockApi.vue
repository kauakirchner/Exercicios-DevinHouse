<template>
  <div class="container">
      <router-view></router-view>
      <h1>Consulta em api por id</h1>
      <div>
          <form @submit.prevent="save">
              <input type="text" placeholder="Nome" v-model="user.nome" class="form-control">
              <input type="text" placeholder="Idade" v-model="user.idade" class="form-control">
                <input type="text" placeholder="email" v-model="user.email" class="form-control">
              <button type="submit">Salvar</button>
          </form>
      </div>
  </div>
</template>

<script>

export default {

    data(){
        return{
            user:{} 
        }
    },
    methods:{
         save(){
           this.$store.dispatch('module1/save', this.user)
           .then(() =>{
               this.$router.push('/retorna')
           })
           console.log('Finalizou o metodo')
       },

        vaiParaHome(){
            this.$router.push('/home')
        }
    }
}

</script>

<style>

</style>