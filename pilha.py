

class Pilha:

    def __init__(self):
        self.pilhas = []
        self.topo = 0


    def vazia(self):
        return self.topo == 0 


    def empilhar(self,valor):

    
        self.pilhas.append(valor)
        self.topo+=1


    def desempilhar(self):
        self.topo-=1
        valor = self.pilhas[self.topo]
        self.pilhas[self.topo]= None 
        return valor 




    
    def __str__(self):

    

        return "Topo -> " + " -> ".join(map(str, reversed(self.pilhas))) + " -> Base"



MinhaPilha = Pilha()
MinhaPilha.empilhar(2)
print(MinhaPilha)