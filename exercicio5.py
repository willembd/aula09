senha = 0
while senha != 1234:
    senha = int(input("Digite a senha: "))

    if senha != 1234:
        print("Senha incorreta!!")

print("Acesso liberado")