# from fila_sequencial_circular import Fila, FilaError
from fila_encadeada import Fila, FilaError
from aluno import Aluno

fila = Fila()
try:
    for i in range(1, 7):
        fila.enfileira(Aluno('aaa',i*10))
except FilaError as fe:
    print(fe)

print(fila)
chave = Aluno('',60)
print('Pesquisa: ', fila.pesquisa(chave))


print(fila.desenfileira())
print(fila.desenfileira())

print(fila)

print('Frente:', fila.elemento_da_frente())

while not fila.vazia():
    print(fila.desenfileira())