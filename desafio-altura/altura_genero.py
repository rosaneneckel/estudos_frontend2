maior_altura = 0
menor_altura = 2
soma_altura_homens = 0
media_altura_homens = 0
qtde_homens = 0
qtde_mulheres = 0

for i in range(1,16):
    print("Pessoa ", i)
    altura = float(input("Digite a sua altura (Ex: 1.60): "))
    genero = str(input("Digite o seu genero (Ex: H ou M): "))

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura

    if genero.upper() == "H":
        soma_altura_homens += altura
        qtde_homens += 1
        media_altura_homens = soma_altura_homens/qtde_homens
    else:
        qtde_mulheres += 1

print("-" * 30)
print("Maior Altura é:", maior_altura)
print("Menor altura é: ", menor_altura)
print(f"A altura média dos homens é: {media_altura_homens:.2f}")
print("A quantidade de mulheres é: ", qtde_mulheres)