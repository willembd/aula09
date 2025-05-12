soma=0
for i in range(5):
    n = int(input(f"Digite a {i+1} nota: "))
    soma = soma + n

media = soma /5
print(f"A média da turma é: {media}")