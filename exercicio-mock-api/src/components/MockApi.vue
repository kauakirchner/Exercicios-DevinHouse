<template>
  <div class="container">
      <h1>Consulta em api por id</h1>
      <input type="number" v-model="id">
      <div class="btn">
          <button @click="consultaApi">Consultar</button>
      </div>
      {{user}}
  </div>
</template>

<script>

import axios from 'axios'
export default {
    name: 'MockApiA',

    data(){
        return{
            id: null,
            user:{} 
        }
    },
    methods:{
        async consultaApi(){
            const promisse = axios.get(`https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users/${this.id}`)
            await promisse.then((response) =>{
            this.user = response.data
            console.log(response.data)
            }).catch((err) =>{
                console.log(err)
                alert('Mano deu erro')
            })
        },
    }
}

</script>

<style>

</style>