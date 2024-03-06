"""
# inverter palavra
palavra = "mundo"
palavra_invertida = ""


x = len(palavra) - 1
# enquanto x for maior ou igual a zero entre no while
while x >= 0:
    palavra_invertida += palavra[x]
    x -= 1
print(palavra_invertida)"""

# remove duplicados
"""listagem = [1, 1, 2, 3, 4, 'teste', 'maria',
            'joao', 'cleber', 'teste', 'teste', 'teste', 'teste', 'teste']
listagem_duplicados = []
listagem_final = []
for chave, valor in enumerate(listagem):
    if valor in listagem_final:
        listagem_duplicados.append(valor)
    else:
        listagem_final.append(valor)
print(listagem_final)"""


# capitalize, torna primeira letra maiuscula
# [::-1] inverte list
# a função list('teste') converte o paramentro 'teste' em lit de caracter
# sorted em python ordena primeiro as maiusculas
"""escola = sorted(list('danilo'.capitalize())[::-1])
print(escola[3])"""

# desafio FizzBuzz
"""x = 1
while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
    x += 1"""


# rotacionar uma lista
lista = [1, 2, 3, 4, 5, 6, 7]
lista_clone = []
rotacionar = 3

while rotacionar > 0:
    for chave, valor in enumerate(lista):
        if chave == 0:
            ultimo_item = len(lista)-1
            lista_clone.append(lista[ultimo_item])
        elif chave == (len(lista)-1):
            lista_clone.append(lista[chave-1])
            lista = list(lista_clone)
            lista_clone = []
        else:
            lista_clone.append(lista[chave-1])

    rotacionar -= 1
print("lista depois for", lista)

"""for chave, valor in enumerate(lista):
    # print("tamanho :: ", len(lista))
    print(chave, valor)

    # if rotacionar < 0 and (len(lista)-1) == chave:
    if chave == 0:
        print("ultimo item")
        lista_clone[0] = lista[len(lista)-1]
        lista_clone[1] = valor
    else:
        # lista = [1, 2, 3, 4, 5, 6, 7]
        print("item :: ", chave)
        lista_clone[chave+1] = valor

    rotacionar -= 1

print("lista_clone", lista_clone)"""
