# Índice

- [Tipo de Dados](#tipo-de-dados)
- [Estrutura de Dados](#estrutura-de-dados)
- [Geradores](#geradores)

1.  Tipo de Dados

1.  Estrutura de Dados

    - Listas

      - Lista ordenadas e mutaveis

        > list com valores de tipos diferentes não podem ser ordenados

        ```python
             items_list = [1,'teste',34,33]
             resultado = [item for item in items_list if isinstance(item, int)]
        ```

        ```python
             items_list = [1,'teste',34,33]
             resultado = []
             for item in items_list :
                 if isinstance(item, int) :
                     resultado.append(item)

             return resultado
        ```

        - compreensão

                ```python
                    produtos = {"maçã": 30, "banana": 15, "abacate": 80, "manga": 55}
                    produtos_desconto = {produto : valor-((20/100) * valor) for produto, valor in produtos.items() if valor > 50}
                ```

    - Tuplas

      - Lista ordenadas e imutaveis

            ```python
                configuracoes = ('192.168.1.1',8080,'http')
                print ("ip :: ", configuracoes[0])
            ```
            >iteração com for
            ```python
                configuracoes = ('192.168.1.1',8080,'http')
                for item in configuracoes :
                    print (item)
            ```

            >iteração com for e enumerate
            ```python
                configuracoes = ('192.168.1.1',8080,'http')
                for index, item in enumerate(configuracoes) :
                    print (f"{index}: {item}")
            ```

    - Dicionários

      - Armazena pares de chave-valor, mutavel e não ordenavel

        ```python
            dicionario = {'nome':"joao","email":"joao@joao.com.br"}
            print ("nome :: ", dicionario['nome'])
        ```

      - Iterar sobre chave

        ```python
            dicionario = {'a':1,'b':2,'c':3}
            for chave in dicionario :
                print (chave)
        ```

      - Iterar sobre valores

        ```python
            dicionario = {'a':1,'b':2,'c':3}
            for valor in dicionario.values():
                print (valor)
        ```

      - Iterar sobre chaves e valores

        ```python
            dicionario = {'a':1,'b':2,'3':c}
            for chave, valor in dicionario.items():
                print (f"{chave} : {valor}")

        ```

      - Iterar usando enumerate

        ```python
            dicionario = {'a':1,'b':2,'3':c}
            for indice, (chave,valor) in enumerate(dicionario.items()):
                print (f"{indice} : ({chave} -> {valor})")
        ```

      - Compreensão de dicionario

        ```python
            dicionario_alterado = {chave: valor**2 for chave, valor in dicionario.items()}
        ```

      - Iterar sobre chaves ordenadas

        ```python
            dicionario = {'a':1,'b':2,'c':3}
            for chave in sorted(dicionario):
                print (f"{chave} {dicionario[chave]}")
        ```

      - Iterar sobre valores ordenados

        ```python
            dicionario = {'a':1,'b':2,'c':3}
            for chave in sorted(dicionario, key=dicionario.get):
                print (f""{chave}: {dicionario[chave]}")
        ```

      - Iterando com filter em dicionario

        ```python
            for chave in sorted(lambda k: dicionario[k] > 1, dicionario) :
                print (f"{chave} -> {dicionario[chave]})
        ```

    - Conjuntos (Sets)

1.  Geradores

    - Exemplo de uso do yield, atravez de uma função de leitura de arquivo de log

      - em vez de ler todo o arquivo, ele é lido linha por linha, armazenando na memoria, apenas a linha atual que esta sendo lida, na proxima linha ele descarta a anterior e quarda a atual na memoria

      ```python
          def ler_arquivo (arquivo) :
              with open(arquivo,"r") as file :
                  for linha in file :
                      yield linha.strip()


          for linha in ler_arquivo ('arquivo.txt') :
              print (f"{linha}")
      ```

1.  Operadores

    - Aritimeticos

      - Adição : `+`
      - Subtração : `-`
      - Multiplicação : `*`
      - Divisão : `/`
      - Módulo : `%` > resto da divisão
      - Exponenciação : `**`
        ```
            2**3 = 8
        ```

    - Atribuição

      - Atribuição : `=`
      - Atribuição com adição : `+=` (x+=3) o mesmo que (x=x=+3)
      - Atribuição com subtração : `-=` (x-=3) o mesmo que (x=x-3)
      - Atribuição com multiplicação : `*=` (x*=3) o mesmo que (x=x*3)
      - Atribuição com módulo : `%=` ()
      - Atribuição com Exponenciação : `%=` (x%=3) e o mesmo que (x=x%3)

    - Comparação

      - Igual : `==`
      - Não igual `!=`
      - Maior que `>`
      - Menor que `<`
      - Maior ou igual a `>=`
      - Menor ou igual a `<=`

    - Lógicos

      - E : `and`
      - Ou : `or`
      - Negação : `not`

    - Identidade

      - É : `is`
      - Não é : `is not`

    - Associação

      - Em : `in`
      - Não em : `not in`

    - Bit a Bit
      - E
      - Ou
      - Xor
      - Deslocamento para esquerda
      - Deslocamento para direita
      - Inversão

1.  Decoradores

    - Modifica o comportamento de uma função ou metodo

    ```python
        import time

        def calcula_valor (valor1,valor2) :
            return valor1+valor2

        def calcula_valor_decorador (func) :
            def wrapper (*args, **kwargs):
                inicio = time.time()
                resultado = func(*args, **kwargs)
                fim = time.time()
                tempo_decorrido = fim - inicio
                print (f"{func.__name__} levou {tempo_decorrido:.4f} segundos para executar")
                return resultado
            return wrapper


        print (calcula_valor(1,2))
    ```

1.  Funções e Metodos

    - Funções são independentes
    - Metodos são funções dentro de uma classe, depende da classe para existirem e atuarem.

1.  Condições

    ```python
        if x == 1 :
        else :

        if x == 1 :
        elif x == 2 :
        else

        if x==1 and x == 2 :
    ```

1.  Loops

    ```python
        # normalmente usado em listas pre definidas ou finitas
        for item in items:
            print (f"{item}")

        # norlmalment usado quando não se sabe quando a condição ou quantidade de loops
        while x == 123 :
            x = input(">")
            print (f"Você pressionou '{x}'. continue pressionando")

    ```

1.  Classes

    ```python
        class Carro :
            def __init__ (self,marca, modelo, ano) :
                self.marca = marca
                self.modelo = modelo
                self.ano = ano

            def descricao (self) :
                return (f"{self.marca} {self.modelo} {self.ano}")


    ```

1.  Erros e Exceções

    - Erros
      - Problemas que acontecem no python durante a compilação, antes da execução. Erros de sintaxe.

    ```python
        if True
            Print ("error de sintaxe, falta dos dois pontos.")
    ```

    - Exceções, erros que não são fatais.

    ```python
        try:
            resulta = 10 / 0
        except ZeroDivisionError:
            print ("Não é possivel dividir por zero")
    ```

    - Tratamento

    ```python
        try:
            numero = int (input("Digite um número:"))
            inverso = 1 / numero
        except ValueError:
            print ("Você não digitou um número válido.")
        except ZeroDivisionError :
            print ("Zero não tem inverso.")
        else :
            print (f"o inverso de {numero} é {inverso}.")
        finally :
            print ("Execução do módulo finally.")
    ```

    ```python
        x = -1
        if x < 0 :
            raise ValueError("o x não pode ser negativo.")
    ```

1.  Modulos e Pacotes

    - Módulo Simples

    ```python
        # matematica.py
        def soma (value1,value2) :
            return value1+value2


        # calculos.py
        import matematica

        resultado = matematica.soma(1,2)
        print (f"{resultado}")
    ```

    - Pacote

    ```python
        # matematica /
        #           __init__.py
        #           basico.py
        #           avancado.py

        # basico.py
        def soma (value1,value2) :
            return value1+value2


        # avancado.py
        def exponenciacao (value, exponente):
            return value**exponente

    ```

1.  Ambientes Virtuais
    - venv
    ```bash
        python3 -m venv myprojectenv
    ```
1.  Entradas e Saida

1.  design patterns

    - Singleton

      - Class com apenas uma instacia, exemplo : Class Database

    - Factory Method

    - Adapter

      ```bash
          python3 -m venv myprojectenv
      ```

    - Observer

    - Decorator

    - Strategy

1.  PEP 8

1.  Testes unitários

1.  Testes de Integração

1.  Arquitetura de microserviços

1.  Shell Script

1.  Big-o notation
