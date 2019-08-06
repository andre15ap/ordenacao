import csv , io
import time
import gerar_lista
import sys

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


lista_tamanho = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000]

# saida = open('saidas/selection_aleatorio.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)


# for i in lista_tamanho:
#     lista = gerar_lista.aleatoria(i)
#     inicio = time.time()
#     resultado = selectionSort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])

# saida = open('saidas/selection_inverso.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)


# for i in lista_tamanho:
#     lista = gerar_lista.inversa(i)
#     inicio = time.time()
#     resultado = selectionSort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])

saida = open('saidas/selection_ordenado.csv', 'w', newline='')
saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)


for i in lista_tamanho:
    lista = gerar_lista.ordenada(i)
    inicio = time.time()
    resultado = selectionSort(lista)
    fim = time.time()
    tempo = fim - inicio

    saida_csv.writerow([i, '{:.5f}'.format(tempo)])