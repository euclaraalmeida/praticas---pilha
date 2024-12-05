'''Editor de Pilha v1.2
=====================================

Pilha Selecionada: 3 de 10

[ ] <- topo
=====================================

(e) Empilhar

(d) Desempilhar

(t) Tamanho

(o) Obter elemento do topo

(v) Teste de pilha vazia

(r) Criar nova Pilha

(n) Inverter os elementos da pilha

(z) Esvaziar a pilha

(c) Concatenar duas pilhas

(m) Escolher outra pilha

(n) Conversão dec/bin

(s) Sair
=====================================

Digite sua opção: [ _ ]


'''

import numpy as np


class Pilha:

    def __init__(self, tamanho:int = 3):

        self.tamanho_lista = 1
        self.pilhas = [np.full(tamanho, None)]
        self.topos = [0] * len(self.pilhas)

    def tamanho_pilhas(self,pilha_escolhida):
        return len(self.pilhas[pilha_escolhida])

    def tamanho_array(self):
        return len(self.topos)

    def vazia(self,pilha_escolhida):
        return self.topos[pilha_escolhida] == 0
      

    def cheia(self,pilha_escolhida):
        return self.topos[pilha_escolhida] == (len(self.pilhas[pilha_escolhida]))

   

    def empilhar(self,valor,pilha_escolhida):

        if self.cheia(pilha_escolhida):
            return ('a pilha esta cheia')

        self.pilhas[pilha_escolhida][self.topos[pilha_escolhida]] = valor
        self.topos[pilha_escolhida]+=1


    def Desempilhar(self,valor,pilha_escolhida):

        if self.vazia(pilha_escolhida):

            print(' a pilha esta vazia')


        self.topos[pilha_escolhida]-=1

        valor = self.pilhas[pilha_escolhida][self.topos[pilha_escolhida]]
        self.pilhas[self.topo] = None

        return valor 

    
    def NovaPilha(self, tamanho:int = 3):
        self.tamanho_lista+=1
        self.pilhas.append(np.full(tamanho, None)) 
        self.topos.append(0)
        

    def __str__(self):

        if self.vazia(pilha_escolhida):

            return "Pilha vazia"

        return "Topo -> " + " -> ".join(map(str, reversed(self.pilhas))) + " -> Base"
        
    def topo(self,pilha_escolhida):
        return self.pilhas[pilha_escolhida][self.topos[pilha_escolhida]-1]

    def inverter(self):
        self.aux_pilha = []

        while not self.pilhas[pilha_escolhida].vazia():
            self.aux_pilha.append(self.pilhas[pilha_escolhida])

        return aux_pilha



minha_pilha=Pilha()


minha_pilha.empilhar(2,0)