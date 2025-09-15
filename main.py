import json

data = json.load(open("usuarios.json"))

def main():
    print("bem vindo ao sistema de login")
    usuarioInput = input("Digite o usuario: ")
    senhaInput = input("Digite a senha: ")

    tentativasCount = 3
    senhaFound = False
    usuarioFound = False

    while tentativasCount <= 0:
        tentativasCount -= 1 
        for usuario in data:
            if usuario["usuario"] == usuarioInput and usuario["senha"] == senhaInput:
                usuarioFound = True
                senhaFound = True
                break
            elif usuario["usuario"] == usuarioInput and usuario["senha"] != senhaInput:
                usuarioFound = True
                senhaFound = False
            elif usuario["usuario"] != usuarioInput and usuario["senha"] == senhaInput:
                usuarioFound = False 
                senhaFound = True
            else:
                usuarioFound = False 
                senhaFound = False
    if senhaFound and usuarioFound:
        print("Entrou no sistema") 
    elif usuarioFound:
        print("senha incorreta")
    else:
        print("Usuario nao encontrado")

def onLogin():
    pass
main()