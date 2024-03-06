1. Sintaxe e Conceitos Básicos

- O que são listas, tuplas, dicionários e conjuntos em Python e como diferem entre si?
- Listas são um conjunto de elementos, ordenaveis e mutais.
- Tuplas são um conjunto de elementos, não ordenaveis e imutaveis
- Dicionarios são um conjunto de chaves e valores, ordenaveis e mutaveis
- Conjuntos ....

- Como você pode gerar números aleatórios em Python?
  import random

        print (random.random())

- Explique a diferença entre == e is.
  == é um operador de atribuição
  is é um operador de identidade

2.  Estruturas de Dados

    - Como você inverteria uma string em Python?

      ```python
         palavra = "mundo"
         palavra_invertida = ""


         x = len(palavra) - 1
         # enquanto x for maior ou igual a zero entre no while
         while x >= 0:
             palavra_invertida += palavra[x]
             x -= 1
         print(palavra_invertida)

      ```

    Dado uma lista, como você removeria elementos duplicados?

    ```python
        # remove duplicados
        listagem = [1, 1, 2, 3, 4, 'teste', 'maria',
                    'joao', 'cleber', 'teste', 'teste', 'teste', 'teste', 'teste']
        listagem_duplicados = []
        listagem_final = []
        for chave, valor in enumerate(listagem):
            if valor in listagem_final:
                listagem_duplicados.append(valor)
            else:
                listagem_final.append(valor)
        print(listagem_final)
    ```

    Como você pode ordenar um dicionário por valores?

    ```python
        dicionario = {'um':1,'quatro':4,'dois':2,'dez':10}
        dicionario_sorted = sorted(dicionario.items(),key lambda item:item[1])
        dicionario_sorted = dict(dicionario_sorted)
    ```

3.  Funções e Programação Orientada a Objetos

    - O que é um decorador e como você o usaria?
      Decorador é um scrip ou uma função que modifica o comportamento de uma função.

    - Como você pode criar uma classe em Python? Explique o conceito de herança.

      ```python
          # class to calculate installments
          class CalculateInstallment():
              # constructor
              def __init__(self, total_value, period):
                  self.total_value = total_value
                  self.period = period

              def calculate (self) :
                  installment_value = self.total_value/period
                  return installment

      ```

      Class é uma estrutura que permite você criar objetos, que podem representar um objeto da vida real, uma situação como uma venda, um produto e etc.
      Herança é uma forma de criar uma class, onde essa classe herda atribuitos e metodos de outra class, exemplo :

      ```python
          class Pessoa:
              def __init__ (self, full_name)
                  self.full_name = full_name

              def show_data (self)
                  print (f"full name {self.full_name}")


          class fisica(Pessoa):
              def __init__(self, full_name, cpf) :
                  self.full_name = full_name
                  self.cpf = cpf

              def show_data (self) :
                  print (f"full name fisica {self.full_name} cpf {self.cpf}")

      ```

    - O que são métodos mágicos em Python, e pode dar um exemplo?
      São metodos que podem ser criados para sobrecarregar outro metodo padrão, exemplo;
      se eu quero somar atributos ou metodos de instancias, eu posso criar um metodo **add**,
      quando eu na expressão de soma usando o simbolo "+" a classe vai proucurar o metodo **add**,
      encontraando ele realiza o fluxo e retorna.

4.  Compreensão de Listas e Expressões Geradoras

    - Dê um exemplo de como você usaria a compreensão de listas.

    ```python
         lista = [1,3,55]
         lista_novo = [item for item in lista if item < 5]
    ```

    Qual é a diferença entre uma compreensão de lista e uma expressão geradora?

    - A compreeção de lista constroi outra lista atravez de um iteravel (consome mais memoria)
      A compreensão de lista armazena toda a lista em memoria, para uso imediato de toda ela, com isso consumindo mais memoria.
      A empressão geradora, armazena só o loop atual trabalhando sob demana, consumindo menos memoria, sendo mais ultilizada para quantidade
      elevadas de dados.

5.  Gerenciamento de Erros e Exceções

    - Como você pode capturar e tratar uma exceção em Python?
      Abaixo um exemplo:

      ```python
          def soma_numeros (x,y) :

              try :
                  resultado = x + y
                  return resultado
              except TypeError as e
                  return str(e)

         soma_numeros (1,2) # resulta em 3
         soma_numeros ('tex',1) # resulta em erro

      ```

    - Explique a utilidade de finally em blocos try-except.
      Bloco de script que sera executado independente/sempre se house exceção ou não.

6.  Módulos e Pacotes

    - Como você importaria um módulo específico de um pacote ?

    ```python
        from financa import algebra
    ```

    - Qual é a diferença entre **init**.py e **main**.py?
      Marca diretorio como sendo de um pacote do tipo python
      Ponto de entrada de um pacote

7.  Manipulação de Arquivos

    - Como você leria um arquivo de texto linha por linha em Python?

      ```python
          file_path = "arquivo.txt"
          with open(file_path, "r") as file:
              for line in file :
                  print (line.strip())


              def get_line_like_generator () :
                  file_path = "arquivo.txt"
                  with open(file_path,"r") as file
                      for line in file :
                          yield line.strip()


              for line in get_line_like_generator() :
                  print (line)
      ```

    - Explique como escrever dados em um arquivo em Python.

      ```python
          file_path = "arquivo.txt"
          with open (file_path) as file :
              file.write("novo conteudo \n")

      ```

8.  Operações com String

    - Como você pode formatar strings em Python?

      ```python
        # usando
        # resultado = "joao casou com %s" % nome

        # usando str.format
        # resultado = "joao casou com {}".format(nome)

        # usando a função interna "f"
        # exemplo : f"texto ser formatado {variavel}"
      ```

      - Dê um exemplo de como você usaria expressões regulares em Python.

      ```python
        import re

        # encontrando todas as correspondencias de um padrão
        texto = "Contatos: john@example.com, jane.doe@example.com""
        emails = re.findAll(r'\b[A-Za-z-9._%+-]@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',texto)

        # check string de acordo com padrão
        telefone = re.match(r'\(\d{3}\) \d{3}-\d{4}')
      ```

9.  Multithreading e Multiprocessing

    - Qual é a diferença entre multithreading e multiprocessing?
      Multitread é a execução de processos em mais de uma thread ou linhas de execução

    - Como você pode executar uma função em um thread separado?

10. Decoradores, Geradores e Iteradores
    - O que é um iterador e como você pode criar um em Python?
      Iterador é um objeto (FOR) que permite percorrer item a item coleções (list, dict, tupla e set).
      ```python
            lista = [1,2,5,66,44,32]
            for item in lista :
                print(item)
      ```
      - Dê um exemplo de um gerador e explique como ele funciona.
        É uma função que retorna um objeto iterador, que pode ser usado o for. Geradores permitem pausar a iteração e voltar nela depois, isso pode ser feito usando a palavra chave : yield.
        Normalmente usado em grande conjuntos de dados como logs. Outro ponto importante é que ele
        não armazena toda a coleção na memoria, apenas a atual que esta sendo trabalhada. Economizando
        memoria.
11. Testes
    Como você realizaria testes unitários em seu código Python?
    O que é um assert em Python, e como ele é utilizado?

12. SOLID

    - S (SPR) : Single Responsibility Principle (Principio da Responsibilidade Unica)

      - Classe com uma unica responsibilidade

    - O : Open-Closed Principle (Princio Aberto Fechado)

      - Aberto para extensão e fechado pra modificação

    - L : Liskov Substitution Principle (Principio da Substituição de Liskov)

      - a

    - I : Interface Segregation Principle (Principio da Segregação da Interface)
      - a
    - D : Dependecy Invertion Principle (Principio da Inversão da Dependencia)
      - a

# analisar relação entre

solid
clean code
ddd
