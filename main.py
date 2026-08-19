from dados.cadastro import cadastar 

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
                    print(cadastar())
                    user = cadastar()
                case 2:
                    ler_usuarios(user)
                case 3:
                    print("oi") 
                case 4:
                    print("Saindo... Volte sempre!")
                    break
                case _:
                    print("Opção não existe!")

        except(TypeError, ValueError):
            print("Opção inválida. Tente novamente!")
                