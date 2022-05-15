class Cliente{
    constructor(nome, cpf, cnpj, endereco, numeroTelefone){
        this.nome = nome;
        this.cpf = cpf;
        this.endereco = endereco
        this.numeroTelefone = numeroTelefone
        this.cnpj = cnpj

    }

     get chamaValidacaoCpf(){
        return this.isValidCpf()

    }
    get chamaValidacaoCnpj(){
        this.isValidCnpj()
    }

    isValidCpf(){
        if(this.cpf.length !== 11){
            return 'CPF inválido!!'
            
        }
        else{
            return 'CPF válido'
        }
        
        
    }
    isValidCnpj(){
        if(this.cnpj.length !== 14){
            return 'CNPJ inválido!!'
        }
        else{
            return 'CNPJ válido!'
        }
      
    }
    
}

const testeCpf = new Cliente('Kauã', 11111111111, 1111111111111, 'Casa do Kauã', 40028922 );


console.log(testeCpf)
