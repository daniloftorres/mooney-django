# estrutura de dados 

## list ordenavel e mutavel
print ("###### Bloco de List")
frutas = [] # criando list vazio
frutas2 = ['mamao','melancia'] # criando list 2
frutas.append('laranja') # adicionando item 
#todas_frutas = frutas  + frutas2
frutas.insert(1,'pera')
frutas.extend(frutas2)
frutas.pop(0)
del frutas[0]
frutas.sort()
print ("")

## dict nao ordenado, mutavel
print ("###### Bloco de Dict")
cliente = {}
cliente2 = {}
#todos_nome = 
cliente['nome'] = "José"
cliente.update(cliente2)
print ("dict antes do pop",cliente)
#cliente.pop('nome')
print(cliente.get('nome'))

print ("dict antes do for",cliente)
for k in cliente.keys() : 
    print (k)
for v in cliente.values() :
    print (v)
for k,v in cliente.items() : 
    print (k,v)
print ("")

#tupla não ordenavel, não mutavel
print ("###### Bloco de Tupla")
tuplas = ('jose',1,[2]) 
print(tuplas[0])
print(len(tuplas))
print(tuplas.count("jose"))
print (tuplas)
print (type(tuplas))
print(tuplas.index(1))
print ("")

print ("###### Bloco de conjuntos set mutavel")
conjunto = {}
print (type(conjunto))
conjunto = {1,2}
print (type(conjunto))
conjunto.add('maria')
conjunto.update(frutas)
#conjunto.remove('maria')
print(conjunto.pop())
print (conjunto)
conjunto.clear()
print (conjunto)
print ("")

print ("###### Bloco de conjuntos fronzenset imutavel")
# o mesmo que set, mas nao aceita adicionar ou remover imutavel

print ("###### Bloco de Deque")
from collections import deque

fila =  deque(maxlen=10)
fila.append(1)
fila.append(2)
fila.appendleft(3)
print (fila)
fila.pop()
fila.popleft()