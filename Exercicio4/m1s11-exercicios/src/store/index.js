import axios from 'axios'
import {createStore} from 'vuex'

const moduloSave = {
    namespaced: true,
    state(){
        return{
            users:[]
        }
    },
    actions:{
       async save(context, users){
           await axios.post('https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users', users)
           .then((response) =>{
               console.log(response)
           }).catch((error) =>{
               console.log(error)
           })
        }
    }
}

const moduloLoad = {
    namespaced: true,

    state(){
        return{
            users:{}
        }
    },
    actions:{
        load(context){
            axios.get('https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users')
            .then((response) =>{
                context.state.users = response.data
            })
        }
    }
}

const store = createStore({
    modules:{
        moduloSave,
        moduloLoad
    }
})

export default store

