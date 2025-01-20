class FilaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)


class Node:
    
    def __init__(self,carga):
        self.carga = carga
        self.prox = None

class Controle:

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0

class Fila:

    def __init__(self):
        self.__head = Controle()


    def tamanhoFila(self):
        return self.__tamanho

    def vazia(self):
        return self.__tamanho == 0

    def primeiroDaFila(self):
        return self.__head.primeiro.carga

    def enfileirar(self,valor):
        novo = Node(valor)
        
        if self.vazia():
            self.__head.primeiro = self.__head.ultimo = novo #ponteiros apontando para o unico nó
        else:
            self.__head.ultimo.prox = novo # o prox da carga 3 agora vai apontar para a carga 4
            self.__head.ultimo = novo # a carga 3 vai apontar para a carga 4 

        self.__tamanho +=1

    def desenfileira():
        valor_removido = primeiroDaFila()

        if self.vazia():
            return FilaError('Fila vazia')
        elif tamanhoFila() == 1:
            self.__head.primeiro = self.__head.ultimo = None 
        else:
            self.__head.primeiro = self.__head.primeiro.prox

        self.__tamanho-=1
        return valor_removido

    def pesquisar(self,valor):
        cursor = self.__head.primeiro
        while cursor is not None:
            cursor = self.prox 






