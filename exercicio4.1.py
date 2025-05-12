
soma=0
media=0
for i in range(5):
    n = int(input(f"Digite a {i+1} nota: "))
    soma = soma + n
    media = soma / 5

if media > 7:
    print(f"Media {media} Aprovado")
elif media < 4:
    print(f"Media {media} Rerovado")
else:
    print(f"Media {media} Recuperação")