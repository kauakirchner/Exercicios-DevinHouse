<template>
  <div class="container">
      <router-view></router-view>
      
      <form>
          <input type="text" placeholder="Nome" v-model="user.nome" class="form-control">
          <hr>
          <input type="number" placeholder="Idade" v-model="user.idade" class="form-control">
          <hr>
          <input type="email" placeholder="Email" v-model="user.email" class="form-control">
          <hr>
          <button type="button" class="btn-primary" @click="save">Save</button>
      </form>
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
        this.$store.dispatch('moduloSave/save', this.user)
        .then(() =>{
            this.$router.push('/pessoas')
        })
      
    }
    },
    
}
</script>

<style>

</style>