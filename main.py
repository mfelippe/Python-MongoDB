import mongodb
import os

def new_user():
    print("======================== Cadastro ======================")
    nome = input('digite o nome para o cadastro: ')
    email = input('digite o email para o cadastro: ')
    senha = input('digite uma senha de 6 digitos: ')
    senha = int(senha)
    print('*********** NOVO USUARIO ********* ')
    print("Usuario: ", nome)
    print("Email: ",  email)
    print("Senha: ", senha)
    print("********************************** ")
    mongodb.cadastrar_user(nome,email,senha)
    return

def search():
    print("======================== Buscar ======================")
    parametro = input('digite o parametro que deseja buscar: ')
    dado = input('digite o dado que deseja buscar: ')
    mongodb.buscar_dado(parametro,dado)
    return
def login():
    print("======================== LOGIN ======================")
    mongodb.login()
    return


controle = 0 # váriavel de controle
#menu da aplicação
while(controle == 0):

    print("======================== Banco de Dados MongoDB ======================")
    print("======================== #1 - Login             ======================")
    print("======================== #2 - Cadastro          ======================")
    print("======================== #3 - Busca             ======================")
    print("======================== #4 - Sair              ======================")
    print("======================================================================")
    menu = int(input("digite a opção desejada : "))
    if menu == 1:

        login()
    elif menu == 2:

        new_user()
    elif menu == 3:

        search()
    else:
        print("======================== ADEUS ======================")
        controle = 1