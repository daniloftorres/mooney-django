# Coleções

## List

    - Coleção de Valores, qualquer tipo de valor, ordenado e mutavel.
    lista = [1,3,5,'teste',teste2]

    pop - remove ultimo item
        lista.pop()
    del - renove posição indicada
        lista.del(1)
    insert - insere posição indicada
        lista.insert(1,'hoje')
    append - insere fim lista
        lista.append("amanha")

## Dict

    - Coleção de pares valores com chave -> valor, não ordenado e mutavel

        cliente = {'nome':'Danilo','idadde',37}

        - acessar item
            cliente['nome']
            cliente.get('nome')
        - remover item
            del cliente['nome']
            cliente.pop('nome')

        - iteração
            for k in cliente.keys(): print (k)
            for v in cliente.values(): print (v)
            for k,v in cliente.items(): print (k,v)

        - limpar todo dicionario
            cliente.clear()

        - copia dicionario
            cliente2 = cliente.copy()

        - adicionar novo dict no dict atual
            cliente2 = {'altura':2,peso:80}
            cliente_mesclado = cliente.update(cliente2)

        - popitem
            remove item aleatorio

## Tupla

    - Coleção de valores de diferentes tipos e imutaveis, mesmo conceito de list, mas não pode ser alterado o items
    exemplo: frutas = ('abacaxi','maca','banana')
            aleatorio = ('tess',2,[1,2,3])

    operações
    tupla.index('abacaxi') retorna o index de onde esta o abacaxi
    tupla.count('abacaxi') retorna quantas vezes o abacaxi esta na tupla
    len(tupla) retorna a quantidade de itens

    - acessar item
        frutas[2]

## Set

    - Coleção de valores de qualquer tipo, não repetido e conjuntos em si, são mutaveis, mas o elementos não são.
    exemplo: planeta_anao = {'plutao','ceres'}
    posso remover plutão, e adicionar outro, mas não posso trocar diretamente plutão por outro

## Notação Big O
