cont=0
frase = input("Digite uma frase: ")

for i in range(len(frase)):
    if frase[i] == "a":
        cont+=1

print(f"{cont} letras (a) tem na frase")