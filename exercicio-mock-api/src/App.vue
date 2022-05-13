<template>
  <div class="container">
    <MockApi/>
  </div>
</template>

<script>
import MockApi from './components/MockApi.vue'

export default {
  name: 'App',
  components: {
    MockApi
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
