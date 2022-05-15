export function valorXquantidade(...lista){
    return lista.reduce((a, produtos) =>{
        return a + produtos.quantidade * produtos.valor
    },0)
}