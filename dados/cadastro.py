def cadastrar():
    n = input("Insira seu nome: ")
    while True:
        try:
            i = int(input("Insira sua idade: "))
            if i < 18:
                print("Voçê menor de idade!")
                break
        except(TypeError, ValueError):
            print("Erro. Insira uma idade válida!")
            continue
        else:
            dados = {
                "nome": n,
                "idade": i
            }

    return dados

        