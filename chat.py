import os

mensagens = []

nome = input("Seu nick: ")

while True:

    # limpando terminal
    os.system('cls')

    # mostrando mensagens na tela
    if len(mensagens) > 0:
        for x in mensagens:
            print(x['nome'] + ':', x['texto'])

    print("______________________")

    # obtendo texto
    texto = input("Digite sua mensagem: ")
    if texto == "fim":
        break
    
    # adicionando mensagem na lista
    mensagens.append({
        'nome': '@' + nome,
        'texto': texto,
    })