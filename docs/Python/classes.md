# Classe

    ```python
        class Carro :
    ```

# Objetos

    - Resultado final de uma classe, normalmente é a representatividade de algo como um carro, uma venda ou qualquer coisa que possa
    ser representado, com atributos e valores.

# Metodos

    - são funções dentro de classes

    ```python
        class Pessoa :
            def set_cor (cor):
                self.cor = cor
    ```

# Herança

    - For de construção de classes onde existe uma classe que herda atributos e metodos de outra class.

    ```python
        class Pessoa :
            def __init__ (self,documento, nome) :
                self.documento = documento
                self.nome = nome



        class Cliente(Pessoa):
            pass

    ```

# Construtor

    - metodo que é chamado quando a classe é instanciada
