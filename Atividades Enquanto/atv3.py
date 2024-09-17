contador = 1
soma = 0
totalNegativos = 0

while contador <= 10:
    valor = int(input(f"Informe o valor {contador}: "))

    if valor< 0:
        totalNegativos = totalNegativos + 1
    else:
        soma = soma + valor #soma +=valor

print(f"A soma dos positivos é {soma}")
print(f"O total de negativos é {totalNegativos}")