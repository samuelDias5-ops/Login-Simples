def cadastrar():
    n = input("Insira seu nome: ")
    id = 1
    while True:
        try:  
            i = int(input("Insira sua idade: "))
        except:
            print("Erro. Insira uma idade válida!")
            continue
        else:
            print("Novo Cadastro: ", end="")

        dados = {
            "id": id,
            "nome": n,
            "idade": i
        }
        id+=1
        print(f"{n} cadastrado com sucesso!")
        
        return dados
                    