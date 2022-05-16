<template>
  <div class="container">
    <PessoasA/>
  </div>
</template>

<script>
import PessoasA from './components/PessoasA.vue'

export default {
  name: 'App',
  components: {
    PessoasA
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
