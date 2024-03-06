# Estrutura de Dados

# stack
# > metoso de organizar dados de um modo que fiquem como pilhas, uma em cima da outra
# > primeira elemento é sempre o ultimo colocado
# > fifo, primeiro que entra é o primeiro que sai
# > push :  adicionar um novo elemento no topo da pilha
# > pop : remove o elemento do topo da pilha
# > empty : esta vazia, true or false
# > top : retorna o valor do elemento no topo da pilha sem remove-lo
# > size: tamanho da pilha

# data, next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# top, size


class Stack:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def push(self):
        print("")