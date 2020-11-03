'''
 Arquivos com a funções do bando MongoDb para ser usada na parte pricipal do código

'''
import pymongo
import datetime

client = pymongo.MongoClient(
    "mongodb+srv://admin:MFelippe1@cluster0.q6oxa.mongodb.net/testdb?retryWrites=true&w=majority")
# minha conexao com o db e a coleção
usuario = client.testdb.usuario
def cadastrar_user(nome,email,senha):
    user = {
        "nome" : nome,
        "email": email,
        "senha": senha,
        "lancamento": datetime.datetime.now()
    }
    user_id = usuario.insert_one(user).inserted_id
    print("usuario cadastrado...")
    return user_id
def buscar_dado(parametro,dado):
    resultado = usuario.find_one({parametro:dado})

    if resultado is None:
        print("nenhum resultado encontrado")
    else:
        print(resultado)
    return
def login():
    erro_email = 0; #variavel de controle para tentativa de login

    while (erro_email <=2):
        email = input("digite seu email : ")
        login = usuario.find_one({"email": email})
        if login is None:
            print("Usuario não cadastrado")
            erro_email = erro_email + 1
        else:
            erro_senha = 0 # variavel de controle para as tentativas de senha
            # carregando a senha do dicionario para um variavel senha-temporaria
            senha_temp = int(login['senha'])
            erro_email = 2
            while(erro_senha<=2):
                #caputurando a variavel senha para comparação
                senha = int(input("digite sua senha: "))
                if senha == senha_temp:
                    print("login bem sucedido !")
                    erro_email =3;#sainda do while
                    erro_senha =3;
                else:
                    print("Senha errada")
                    erro_senha=erro_senha+1
                    erro_email = 3
    return
'''
    insert_one = inserção de um dado
    find_one = busca de um dado
    update_one = atualiza um dado
    delete_one = deleta um dado

    os comandos podem ser alterados para _many = para manipular mais dados



user = {
             "nome": "pudim",
             "email": "pudim@gmail.com",
             "senha": 123456,
              "lancamento": datetime.datetime.now()
}
#inserindo dados na coleção
user_id = usuario.insert_one(user).inserted_id

print(user_id)'''
# buscando um dado na coleção
'''
busca = usuario.find_one({"nome": "Mara"})
print(busca)'''
# atualizando um dado
'''
atualizacao = usuario.update_one({'nome': 'Mara'},{'$set':{'nome':'Mazu'}})
print(atualizacao)'''

