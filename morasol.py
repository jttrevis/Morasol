
import random





contas = [123]
agencia_padrao = 999

class Tela():
    def __init__(self, principal):
        print("*****Banco Morasol*****\n")
        print("Como podemos ajudar?\n ----------------- \n")
        opt = int(input("(1) Nova Conta\n ----------------- \n (2) Login\n ----------------- \n  (4) Sair\n ----------------- \n "))
        
        while True:
            try:
                
                if(opt == 1):
                    nova_conta()
                if(opt == 2):
                    login(1,2,3,4,5)
                if(opt == 4):
                    Tela(1)
            except ValueError:
                print("Opcao Invalida")
            continue                
        
    



class Usuario():
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf= cpf
               

class Conta(Usuario):
    def __init__(self, nome, agencia, conta, cpf, saldo):
        Usuario.__init__(self, nome, cpf)
        self.agencia = agencia
        self.conta = conta
        self.saldo = 0
    
    def deposito(self):
        valor_deposito = int(input("Digite o valor do Deposito "))
        if valor_deposito <= 0:
            print("Valor invalido ")
        else:
            self.saldo += valor_deposito
            print(f"Deposito realizado com sucesso, seu novo saldo e: {self.saldo} R$ ")
    
    def sacar(self):
        valor_saque = float(input("Digite o valor de saque: "))
        self.saldo -= valor_saque
        print(f"Saque realizado com sucesso, seu novo saldo e: {self.saldo} R$ ")


        
      
        




# FUNCOES GLOBAIS





def nova_conta():
        print("Por favor entre com seus dados: ")
        nome = input("Nome Completo ")
        genero = input("Genero ")
        cpf = input("Numero do CPF ")
        nova_conta = random.randint(2500, 2599) 
        contas.append(nova_conta)
        agencia = agencia_padrao
        saldo = 0
        print(f"O numero da sua conta e: {nova_conta} ")
        print(f"Sua Agencia e: {agencia_padrao} ")
        print(f"Seu Saldo Atual e: {saldo} ")


        resposta = int(input("Gostaria de Entrar em sua conta? 1 = Sim / 2 = Nao  "))
        if resposta == 1:
            login(1,2,3,4,5)
        else:
            Tela(1)

class login(Conta):
    def __init__(self, nome, agencia, conta, cpf, saldo):
        Conta.__init__(self, nome, agencia, conta, cpf, saldo )
        agencia = int(input("Agencia: "))
        conta = int(input("Numero da Conta: "))

        while True:
            try:
                if conta  in contas and agencia == agencia_padrao:
                        print(f"Login feito com sucesso! \n Bem Vindo! \n Como podemos ajudar? \n ")
                        opt = int(input("(1) Deposito\n ----------------- \n (2) Saque\n ----------------- \n  (4) Tela Inicial\n ----------------- \n "))
                        while True:
                            try:
                
                                if(opt == 1):
                                    Conta.deposito(self)
                                    break
                                if(opt == 2):
                                    Conta.sacar(self)
                                    break
                                if(opt == 4):
                                    Tela(1)
                            except ValueError:
                                print("Opcao Invalida")

                        continue                
            except ValueError:
                    print("Conta ou Agencia invalida! \n Tente novamente!")
                    break
                    
            continue








Tela(1)
        
    






