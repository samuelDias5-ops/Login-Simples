from dados.cadastro import cadastrar, gerar_id
from dados.dados import ler_usuarios, salvar_dados 

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
                    user = ler_usuarios()
                    id_usuario = gerar_id(user)
                    dado = cadastrar(id_usuario)
                    salvar_dados(dado)
                case 2:
                    user = ler_usuarios()
                    for d in user:
                        print(
                                f"ID: {d["id"]} |"
                                f"Nome:\t{d["nome"]} |"
                                f"Idade:\t{d["idade"]}"
                            ) 
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
                