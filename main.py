import json
import time

data = json.load(open("usuarios.json"))
#print(data)

def main():
    print("bem vindo ao sistema de login")
    tentativasCount = 3
    usuarioFound = False

    while tentativasCount > 0:
        usuarioInput = input("Digite o usuario: ")
        senhaInput = input("Digite a senha: ")
        tentativasCount -= 1 
        usuarioIndex = -1
        for usuario in data:
            usuarioIndex +=1
            if usuario["usuario"] == usuarioInput:
                usuarioFound = True
                break
        #print(f"usuarioFound : {usuarioFound} senhaFound : {senhaFound}") 
        if usuarioFound:
            if data[usuarioIndex]["senha"] == senhaInput:
                #print(data[usuarioIndex])

                print("Login realizado com sucesso!\n\n\n\n") 
                tentativasCount = 3
                onLogin(usuarioInput, senhaInput)
                break
            else:
                print("Senha inválida\n\n\n\n")
        else:
            print("Usuario nao encontrado\n\n\n\n")
    if(tentativasCount == 0):
        print("Número máximo de tentativas excedido. Acesso bloqueado.\n\n\n\n")
        time.sleep(30)
        main()

def onLogin(usuario, senha):
    option = 0
    while option != 3:
        print("Selecione uma opção: \n1-Ver perfil \n2-Criar usuário \n3-Sair\n\n\n\n")
        option = int(input("Opção:"))
        match option:
            case 1:
                print(f"Usuário: {usuario} \n Senha: {senha}")

            case 2:
                usuarioRegistro = input("Digite um nome de usuário: ")
                senhaRegistro = input("Digite uma senha: ")
                data.append({"usuario" : usuarioRegistro, "senha" : senhaRegistro})
                json.dump(data, open("usuarios.json", "w"), indent=4)
                print("Usuário registrado!\n\n\n\n")
main()
