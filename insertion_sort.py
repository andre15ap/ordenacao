import csv , io
import time
import gerar_lista


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue



lista_tamanho = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000]


# saida = open('saidas/insertion_aleatorio.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.aleatoria(i)
#     inicio = time.time()
#     resultado = insertionSort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])


# saida = open('saidas/insertion_inverso.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.inversa(i)
#     inicio = time.time()
#     resultado = insertionSort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])

saida = open('saidas/insertion_ordenado.csv', 'w', newline='')
saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

for i in lista_tamanho:
    lista = gerar_lista.ordenada(i)
    inicio = time.time()
    resultado = insertionSort(lista)
    fim = time.time()
    tempo = fim - inicio

    saida_csv.writerow([i, '{:.5f}'.format(tempo)])