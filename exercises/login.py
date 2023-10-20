# guardando os logins
logins = []

while True:
    start = int(input("Bem vindo! Digite 1 para realizar login, 2 para registrar-se e qualquer outro numero para sair: "))

    if start == 1:
        # realizando o login
        print("______________________________")
        username = input("Usuário: ")
        password = input("Senha: ")
        print("______________________________")

        credentials_found = False
        for x in logins:
            if x["username"] == username and x["password"] == password:
                credentials_found = True
        if credentials_found == True:
            print("Login realizado com suceso!")
        else:
            print("Credenciais não encontradas, tente novamente...")

    elif start == 2:

        # registrando       
        print("______________________________")
        reg_username = input("Defina seu usuário: ")
        reg_password = input("Defina sua senha: ")
        print("______________________________")
        logins.append({"username": reg_username, "password": reg_password})
    else:
        break
