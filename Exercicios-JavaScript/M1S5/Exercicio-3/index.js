const produtos = [
    { nome: 'arroz', preco: 9 },
    { nome: 'feijao', preco: 12 },
    { nome: 'batata', preco: 8 },
    { nome: 'macarrao', preco: 5 }
  ];


const getBtn = document.getElementById('btn')

const verificaProduto = (produtoConsultado) =>{
    return produtos.find( i => i.nome === produtoConsultado)
}

getBtn.addEventListener('click', () =>{
    const getP = document.getElementById('DOM')
    const produto = document.getElementById('produto').value;
    const retorno = verificaProduto(produto)
    let alerta = 'O produto não foi encontrado'
    if(retorno){
        alerta = `Valor: ${retorno.preco}`
    }
    else{
        alerta = 'Não tem esse produto aqui'
    }
    getP.innerHTML = alerta

})

const reducer = produtos.reduce((contador, produto) =>{
    return contador + produto.preco
}, 0);

const mostraTotal = document.getElementById('valorTotal')
mostraTotal.innerHTML = `Valor total dos produtos: ${reducer}`
    



