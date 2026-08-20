from dados.cadastro import cadastrar
from dados.dados import ler_usuarios, salvar_dados 
#from dados.salvar import salvar_dados 

def menu_inicial():
    while True:
        print("Sistema de Login")

        print("1- Cadastar Usuário")
        print("2- Ver Usuários cadastrados")
        print("3- Excluir Usuário")
        print("4- Sair")

        try:
            op = int(input("Insira opção: "))

            match op:
                case 1:
                    user = cadastrar()
                    salvar_dados(user)
                case 2:
                    ler_usuarios()  
                case 3:
                    print("oi") 
                case 4:
                    print("Saindo... Volte sempre!")
                    break
                case _:
                    print("Opção não existe!")
        except(ValueError,TypeError, KeyboardInterrupt):
            continue



menu_inicial()
                