import json
import os
from pathlib import Path

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "Database", "user.json")

def salvar_dados(dados):
    if os.path.exists(DB_PATH):
        print("Arquivo dados.py:",Path(__file__).resolve())
        print("BASE_DIR:", BASE_DIR)
        print("DB_PATH:", DB_PATH)
        print("Existe?", DB_PATH.exist())
        try:
            with open(DB_PATH, "r", encoding="utf-8")as arquivo:
                lista = json.load(arquivo)
        except(FileNotFoundError, json.JSONDecodeError):
                lista = []
        lista.append(dados)
        with open(DB_PATH, "w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)

def ler_usuarios(): 
 #       try: 
  #          with open(DB_PATH, "r", encoding="utf-8") as arquivo:
  #              dados = json.load(arquivo)
   #             return dados
            
    #    except(FileNotFoundError, json.JSONDecodeError):
     #       print("Nenhum usuário encontrado.")
  
