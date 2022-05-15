class Transacoes{
    constructor(nmrConta, valorDaTransacao){
        this.nmrConta = nmrConta;
        this.valorDaTransacao = valorDaTransacao;

        
    }
   get transferencia(){
    return this.fazTransferencia
   }

   get deposito(){
    return this.fazDeposito
   }

   fazTransferencia(){
    return `Transferência realizada!, seu saldo agpra é de: ${this.nmrConta -= this.valorDaTransacao}`
   }

   fazDeposito(){
    return `Deposito realizado!, Seu saldo agora é de: ${this.nmrConta += this.valorDaTransacao}`
   }
   
    
}
const transacao = new Transacoes(10002, 2000)


