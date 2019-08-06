import csv , io
import time
import gerar_lista

def merge(llist, rlist):
        """
        Merge two lists into an ordered list.
        """
        final = []
        while llist or rlist:
                # This verification is necessary for not try to compare
                # a NoneType with a valid type.
                if len(llist) and len(rlist):
                        if llist[0] < rlist[0]:
                                final.append(llist.pop(0))
                        else:
                                final.append(rlist.pop(0))

                # This two conditionals here, is for the case when the two lists
                # have diferent sizes. This save us of an error trying to acess
                # an index out of range.
                if not len(llist):
                                if len(rlist): final.append(rlist.pop(0))

                if not len(rlist):
                                if len(llist): final.append(llist.pop(0))

        return final

def merge_sort(list):
        """
        Sort the list passed by argument with merge.
        """
        if len(list) < 2: return list
        mid = len(list) / 2
        mid = int(mid)
        
        return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))


lista_tamanho = [100, 500, 1000, 2000, 3000, 5000, 7000, 10000]

# saida = open('saidas/merge_aleatorio.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.aleatoria(i)
#     inicio = time.time()
#     resultado = merge_sort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])


# saida = open('saidas/merge_inverso.csv', 'w', newline='')
# saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

# for i in lista_tamanho:
#     lista = gerar_lista.inversa(i)
#     inicio = time.time()
#     resultado = merge_sort(lista)
#     fim = time.time()
#     tempo = fim - inicio

#     saida_csv.writerow([i, '{:.5f}'.format(tempo)])


saida = open('saidas/merge_ordenado.csv', 'w', newline='')
saida_csv = csv.writer(saida, delimiter='\t',	quotechar='|', quoting=csv.QUOTE_MINIMAL)

for i in lista_tamanho:
    lista = gerar_lista.ordenada(i)
    inicio = time.time()
    resultado = merge_sort(lista)
    fim = time.time()
    tempo = fim - inicio

    saida_csv.writerow([i, '{:.5f}'.format(tempo)])