import axios from 'axios'
import {createStore} from 'vuex'


const module1 = {
    namespaced: true,
    actions:{
        async save(context, user){
            await  axios.post('https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users', user)
            .then(() =>{
                console.log('Finalizou a promisse')
            })
        },

    }
}

const module2 = {
    namespaced:true,

    state(){
        return{
            users:{}
        }
    },
    actions:{
        load(context){
            axios.get('https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users')
            .then((response) =>{
                console.log(response.data)
                context.state.users = response.data
            })
        },
    }
}

const store = createStore({
    modules:{
        module1,
        module2
    }
    // state(){
    //     return{
    //         users:[]
    //     }
    // },
    // actions:{
    //      async save(context, user){
    //         await  axios.post('https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users', user)
    //         .then(() =>{
    //             console.log('Finalizou a promisse')
    //         })
    //     },
    //     load(context){
    //         axios.get('https://627e989bb75a25d3f3baf486.mockapi.io/api/v1/users')
    //         .then((response) =>{
    //             console.log(response.data)
    //             context.state.users = response.data
    //         })
    //     },
            
        
    // }
})



export default store