for i in range(2, 6):
    print(i)

lista1 = list(range(5, 10))
print(lista1)

lista1 = list(range(0, 10, 3))
print(lista1)

lista1 = list(range(-10, -100, -30))
print(lista1)

texto = "a raposa marrom salta salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)
