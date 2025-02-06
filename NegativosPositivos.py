numero = []

for i in range(10):
    numerounitario = float(input("DIGITE O NUMERO: "))
    numero.append(numerounitario)

quantidade_negativos = 0
soma_positivos = 0

for numerounitario in numero:
    if numerounitario <0:
        quantidade_negativos += 1
    if numerounitario >0:
        soma_positivos += numerounitario

print(f"quantidade de negativos: {quantidade_negativos}")
print(f"soma dos positivos: {soma_positivos}")