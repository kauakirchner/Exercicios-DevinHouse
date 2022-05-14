let vetorNumeros = [1,2,3,4,5,6,7,8,9]
const numerosAoQuadrado = vetorNumeros.map((i) => i ** 2);
console.log('Numeros ao quadrado', numerosAoQuadrado)

const numerosFiltrados = numerosAoQuadrado.filter((i) => i > 30)
console.log('Números filtrados', numerosFiltrados)
