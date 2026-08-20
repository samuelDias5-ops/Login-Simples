def cadastrar():
    n = input("Insira seu nome: ")
    while True:
        try:  
            i = int(input("Insira sua idade: "))
        except:
            print("Erro. Insira uma idade válida!")
            continue
        else:
            print("Novo Cadastro: ", end="")

        dados = {
            "nome": n,
            "idade": i
        }
        print(f"{n} cadastrado com sucesso!")
        return dados
                    