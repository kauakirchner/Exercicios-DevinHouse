class Transacoes{
    constructor(conta,nmrConta,id,data,valorDaTransacao){
        this.conta = conta;
        this.nmrConta = nmrConta;
        this.id = 1;
        this.data = new Date()
        this.valorDaTransacao = valorDaTransacao;


        
    }
   get transferencia(){
    return this.fazTransferencia
   }

   get deposito(){
    return this.fazDeposito
   }

   fazTransferencia(){
       this.id++
    return `Transferência realizada no dia: ${this.data} com o id: ${this.id}, para a conta: ${this.nmrConta} e seu saldo agpra é de: ${this.conta -= this.valorDaTransacao}`
   }

   fazDeposito(){
    return `Deposito realizado!, Seu saldo agora é de: ${this.conta += this.valorDaTransacao}`
   }
   
    
}
const transacao = new Transacoes('Conta do Kauã', 1718, this.id, this.data, 'R$' + 2000);
console.log(transacao)