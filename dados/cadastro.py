def gerar_id(dados):
    if not dados:
        return 1
    return max(d["id"] for d in dados) + 1



def cadastrar(id_usuario):
    n = input("Insira seu nome: ")
    while True:
        try:  
            i = int(input("Insira sua idade: "))
        except:
            print("Erro. Insira uma idade válida!")
            continue
        else:
            print(f"Novo Cadastro: {n} cadastrado(a) com sucesso!")
    
        dados = {
            "id": id_usuario,
            "nome": n,
            "idade": i
        }
       

        return dados
                    