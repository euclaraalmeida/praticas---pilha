# from fila_sequencial_circular import Fila, FilaError
from fila_encadeada import Fila, FilaError

fila = Fila()
try:
    for i in range(1, 7):
        fila.enfileira(i*10)
except FilaError as fe:
    print(fe)

print('Pesquisa: ', fila.pesquisa(50))
print(fila)

print(fila.desenfileira())
print(fila.desenfileira())

print(fila)

print('Frente:', fila.elemento_da_frente())

while not fila.vazia():
    print(fila.desenfileira())