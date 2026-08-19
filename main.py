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

                case 2:
                    ler_usuarios(user)
                case 3:
                    
                case 4:
                    print("Saindo... Volte sempre!")
                    break

        except(TypeError, ValueError):
            print("Opção inválida. Tente novamente!")
                