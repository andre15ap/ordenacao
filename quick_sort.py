import csv , io
import time
import gerar_lista
import sys
sys.setrecursionlimit(1005000)

def quicksort(V):
    if len(V) <= 1: 
        return V
    
    pivot = V[0]
    equal = [x for x in V if x == pivot]
    lesser = [x for x in V if x < pivot]
    greater = [x for x in V if x > pivot]
    return quicksort(lesser) + equal + quicksort(greater)


lista_tamanho = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000]

saida = open('saidas/quick_aleatorio.csv', 'w', newline='')
saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.aleatoria(i)
#     inicio = time.time()
#     resultado = quicksort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])


# saida = open('saidas/quick_inverso.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.inversa(i)
#     inicio = time.time()
#     resultado = quicksort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])


saida = open('saidas/quick_ordenado.csv', 'w', newline='')
saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

for i in lista_tamanho:
    lista = gerar_lista.ordenada(i)
    inicio = time.time()
    resultado = quicksort(lista)
    fim = time.time()
    tempo = fim - inicio

    saida_csv.writerow([i, '{:.5f}'.format(tempo)])