function somaParametrosInfinitos(...parametros){
    return parametros.reduce((a, b) =>{
        return a + b
    },0)
}

export default somaParametrosInfinitos