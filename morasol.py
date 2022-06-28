
import random





contas = []
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
                    Login()
                if(opt == 3):
                    pass
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
    def __init__(self, nome, agencia, conta, cpf):
        Usuario.__init__(self, nome, cpf)
       
        self.agencia = agencia
        self.conta = conta
        global saldo

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


        resposta = input("Gostaria de Entrar em sua conta? S/N ").capitalize
        if resposta == "S":
            Login()
        else:
            Tela(1)

class Login:
    def __init__(agencia, conta):
        while True:
            try:
                if conta  in contas and agencia == agencia_padrao:
                    print("Login feito com sucesso! \n Bem Vindo! \n Como podemos ajudar? ")
            except ValueError:
                print("Conta ou Agencia invalida! \n Tente novamente!")
                    
            continue

Tela(1)
        
    






