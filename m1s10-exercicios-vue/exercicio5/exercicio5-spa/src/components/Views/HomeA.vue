<template>
  <div class="container">
      <h1>Sistema de cadastro de pessoas</h1>
      <div>
          <span>Cadastre agora mesmo</span>
      </div>
      <div>
        <button class="btn btn-primary" @click="irParaCadastro">Ir para cadastro</button>
      </div>
      <router-view></router-view>
  </div>
</template>

<script>
export default {
    methods:{
        irParaCadastro(){
            this.$router.push('/cadastro')
        }
    }
}
</script>

<style>

</style>