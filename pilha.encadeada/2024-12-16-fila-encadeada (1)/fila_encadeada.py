class FilaError(Exception):
    def __init__(self, messagem:str):
        super().__init__(messagem)


class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return f'{self.carga}'


class Controle:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanho = 0


class Fila:
    def __init__(self):
        self.__head = Controle()


    def vazia(self):
        return self.__head.head == None
        # return self.__head.tamanho == 0
    
    def elemento_da_frente(self)->any:
        '''Retona o conteúdo que está na frente da fila, 
           sem removê-lo.'''
        if self.vazia():
            raise FilaError('Não há elementos na fila')
        else:
            return self.__head.head.carga
    
    def pesquisa(self, key:any)->any:
        '''
        Localiza a carga na fila correspondente à chave passada como argumento.
        Se a chave não for encontrada, lança um KeyError
        '''
        cursor = self.__head.head
        while(cursor is not None):
            if cursor.carga == key:
                return cursor.carga
            cursor = cursor.prox
        raise KeyError(f'Chave {key} não encontrada na pilha')

    def elemento(self, posicao:int)->any:
        '''
        Retorna a carga armazenada na posição especificada como argumento.
        Se a posição não existir, lança um FilaError
        '''
        if posicao < 0 or posicao > len(self):
            raise FilaError(f'Posição {posicao} fora dos limites da fila')
        cursor = self.__head.head
        # for i in range(1,posicao):    
        for i in range(posicao-1):
            cursor = cursor.prox
        return cursor.carga

    def enfileira(self, carga:any):
        novo = No(carga)
        if self.vazia():
            self.__head.head = self.__head.tail = novo
        else:
            self.__head.tail.prox = novo
            self.__head.tail = novo
        self.__head.tamanho += 1
    
    def desenfileira(self)->any:
        '''
        Remove o conteúdo que está na frente da fila e retorna-o.
        Lança um FilaError se a fila estiver vazia
        '''
        if self.vazia():
            raise FilaError('Fila vazia. Não é possível remover elementos')
        else:
            # carga = self.__head.head.carga
            carga = self.elemento_da_frente()
            if (len(self) == 1):
                self.__head.head = self.__head.tail = None
            else:
                self.__head.head = self.__head.head.prox
            self.__head.tamanho -= 1
            return carga

    def __len__(self):
        return self.__head.tamanho
    
    def __str__(self):
        s = 'frente->['
        cursor = self.__head.head
        while(cursor):
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s.rstrip(', ')
        s += ' ]<-fim'
        return s
        


    
        
