# coding: utf-8
import csv , io

import time
import gerar_lista

def bubble_sort(lista):
    
    elementos = len(lista)-1
    ordenado = False
    trocas = 0
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False
                trocas +=1        
                # print(lista)
    return lista, trocas



lista_tamanho = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000]

# saida = open('saidas/buble_aleatorio.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.aleatoria(i)
#     inicio = time.time()
#     resultado, trocas = bubble_sort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])

# saida = open('saidas/buble_inverso.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)


# for i in lista_tamanho:
#     lista = gerar_lista.inversa(i)
#     inicio = time.time()
#     resultado, trocas = bubble_sort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])



saida = open('saidas/buble_ordenado.csv', 'w', newline='')
saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)


for i in lista_tamanho:
    lista = gerar_lista.ordenada(i)
    inicio = time.time()
    resultado, trocas = bubble_sort(lista)
    fim = time.time()
    tempo = fim - inicio

    saida_csv.writerow([i, '{:.5f}'.format(tempo)])

