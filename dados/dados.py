import json

def salvar_dados(dados):
    try:
        with open("user.json", "r", encoding="utf-8")as arquivo:
            lista = json.load(arquivo)
    except(FileNotFoundError, json.JSONDecodeError):
        lista = []
    lista.append(dados)
    with open("user.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)



def ler_usuarios(): 
        try: 
            with open("user.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            for dado in dados:
                print(f"{dado['nome']} \t{dado['idade']}")
        except(FileNotFoundError, json.JSONDecodeError):
            print("Nenhum usuário encontrado.")
  
