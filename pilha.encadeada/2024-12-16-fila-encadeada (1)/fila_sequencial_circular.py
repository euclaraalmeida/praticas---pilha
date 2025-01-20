# implementação de uma pilha usando a técnica sequencial
import numpy as np # array numpy

class FilaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)

class Fila:
    def __init__(self, tamanho:int = 10):
        self.__dados = np.full(tamanho, None)
        self.__frente = 0
        self.__fim = -1
        self.__tamanho = 0 # número de elementos ocupados na fila

    def vazia(self):
        return self.__tamanho == 0
    
    def cheia(self):
        return self.__tamanho == len(self.__dados)
    
    def pesquisa(self, key:any)->any:
        '''
        Localiza a carga na pilha correspondente à chave passada como argumento.
        Se a chave não for encontrada, lança um KeyError
        '''
        index = self.__frente
        for _ in range(len(self)):
            if self.__dados[index] == key:
                return self.__dados[index]
            index = (index + 1) % len(self.__dados)
        raise KeyError(f'Chave {key} não encontrada na fila')

    def elemento(self, posicao:int)->any:
        '''
        Retorna a carga armazenada na posição especificada como argumento.
        Se a posição não existir, lança um PilhaError
        '''
        if posicao < 1 or posicao > len(self):
            raise FilaError(f'Posição {posicao} fora dos limites da fila')
        
        index = self.__frente
        for _ in range(posicao-1):
            index = (index + 1) % len(self.__dados)
            
        return self.__dados[index]

    
    def enfileira(self, carga:any):
        if self.cheia():
            raise FilaError('Fila cheia')
        # if self.__final == len(self.__dados)-1:
        #     self.__final = 0
        # else:
        #     self.__final += 1
        self.__fim = (self.__fim + 1) % len(self.__dados)
        self.__dados[self.__fim] = carga
        self.__tamanho += 1

    
    def desenfileira(self)->any:
        '''
        Remove o conteúdo que está no topo da pilha e retorna-o.
        Lança um PilhaError se a pilha estiver vazia
        '''
        if self.vazia():
            raise FilaError('Pilha vazia. Não é possível remover elementos')
        else:
            carga = self.elemento_da_frente()
            self.__frente = (self.__frente + 1) % len(self.__dados)
            self.__tamanho -= 1
            return carga

    def elemento_da_frente(self)->any:
        '''Retona o conteúdo que está na frente da fila, 
           sem removê-lo.'''
        if self.vazia():
            raise FilaError('Não há elemento na frente porque a fila está vazia')
        else:
            return self.__dados[self.__frente] 
    
    def __len__(self):
        return self.__tamanho
    
    def __str__(self):
        s = 'frente->['
        index = self.__frente
        for i in range(len(self)):
            s+= f'{self.__dados[index]}, '
            index = (index + 1) % len(self.__dados)
        s = s.rstrip(', ')
        s += ' ]<-final'
        return s
        


    
        
