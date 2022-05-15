import  Produto  from "./ClasseProduto.js";
import { valorXquantidade } from "./Metodo.js";

const outroProduto = new Produto('Café', 18, 2)
const novoProduto = new Produto('Requeijão', 9, 10)
const maisUmProduto = new Produto('Miojo', 2, 2)
const valorTotal = valorXquantidade(novoProduto, outroProduto, maisUmProduto);
console.log(valorTotal);
console.log(novoProduto, outroProduto, maisUmProduto)
