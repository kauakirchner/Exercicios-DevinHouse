

async function consultaCep(){
    const cep = document.getElementById('cep').value;
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    const result = document.getElementById('retorno');
    const consulta = await fetch(url);
    const enderecoRetornado = await consulta.json()
    result.innerText = JSON.stringify(enderecoRetornado)
        
}


