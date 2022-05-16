import {createStore} from 'vuex'


const store = createStore({
    state(){
        return{
            pessoas:[],
        }
    },
    mutations:{
        cadastraPessoa(state, pessoa){
            state.pessoas.push(pessoa);  
            state.pessoas.sort((x, y) => {
                return Number(x.idade) - Number(y.idade)
              });
        },
      
        deletaPessoa(state, id){
            state.pessoas.splice(id, 1)
        }
    },
})

export default store