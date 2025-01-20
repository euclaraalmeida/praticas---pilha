class PilhaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)


class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'

class Pilha:

    def __init__(self):
        self.__head = None #apenas o ponteiro
        self.tamanho = 0

    def vazia(self):
        if self.__tamanho == 0:
            return True
        return False
        
    def topo(self):
        if self.vazia():
            PilhaError('sua pilha esta vazia')
        return self.__head.carga

    def pesquisa(self,chave): #---> conferir se o valor esta na pilha 

        

    def elemento(self,

    def empilhar(self,valor):
        novo_nó = no(valor) #--> criando um novo nó
        self.prox = self.__head #--> agora o prox é o head(topo) 
        self.__head = novo_nó #--> e o topo agora esta apontando para o novo nó
        self.tamanho+=1

    def desempilha():
        if self.vazia():
            PilhaError('a pilha esta vazia')

        carga = topo() #self.__head.carga --> pegando o ultimo valor
        self.__head = self.__head.prox #apontando para o prox valor do head
        self.tamanho-=1
        return carga #--> nosso valor do topo
