nota = []

for i in range(5):
    notaunitaria = float(input("DIGITE A NOTA DO ALUNO: "))
    nota.append(notaunitaria)

media = 0

for no in nota:
    media = media + no

media = media/5

print(f"media geral: {media}")