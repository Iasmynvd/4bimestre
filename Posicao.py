valores = []

for i in range(10):
    valorunitario = float(input("DIGITE O VALOR:"))
    valores.append(valorunitario)

    posicao = 0

for i in range(10):
        if valores[posicao]<valores[i]:
            posicao = i

print(f"maior valor: {valores[posicao]}")
print(f"posicao do maior valor: {posicao}")