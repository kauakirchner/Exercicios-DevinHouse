<template>
  <div class="container">
      <router-view></router-view>
      <h1>Estamos no componente de cadastro de pessoas!</h1>
      <div class="form">
          <form>
            <div class="row">
                <div>
                <input type="text" placeholder="Nome" class="form-control">
                <hr>
                </div>
                
                <div>
                <input type="email" placeholder="Email" class="form-control"> 
                <hr>
                </div>
                
                <div>
                <input type="number" placeholder="Idade" class="form-control"> 
                </div>                
            </div>
          </form>
          <div class="col-2">
             <div class="col-2">
                <button type="button" class="btn btn-primary">Enviar</button>
            </div>            
          </div>
      </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>

</style>