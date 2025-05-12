numCerto = 8
n=0

while n != numCerto:
    n = int(input("Tente acertar o número secreto: "))
    if n < numCerto:
        print("O número Secreto é maior ")
    elif n > numCerto:
        print("O número Secreto é menor ")
    else:
        print("Parabéns Você Acertou!!")