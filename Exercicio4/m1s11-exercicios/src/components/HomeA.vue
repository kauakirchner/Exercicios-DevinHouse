<template>
  <div class="container">
      <div class="routerView">
        <router-view></router-view>
      </div>
      <div>
        <h1>Não existem Pessoas cadastradas</h1>
        <button @click="irParaInsert">Ir para o cadastro</button>
      </div>
  </div>
</template>

<script>
export default {
    methods:{
        irParaInsert(){
            this.$router.push('/insert')
        }
    }
}
</script>

<style>

</style>