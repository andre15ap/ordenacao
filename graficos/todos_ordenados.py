# coding: utf-8

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Main:
    def __init__(self):
        dataset = open('../saidas/buble_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset.close()


        plt.plot(x, y, label='Booble')

        dataset2 = open('../saidas/insertion_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset2:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset2.close()
      
        plt.plot(x, y, label='Insertion')


        dataset3 = open('../saidas/merge_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset3:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset3.close()
      
        plt.plot(x, y, label='Merge')


        dataset4 = open('../saidas/quick_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset4:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset4.close()
      
        plt.plot(x, y, label='Quick')


        dataset5 = open('../saidas/selection_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset5:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset5.close()
      
        plt.plot(x, y, label='Selection')



        plt.legend()
        plt.grid(True)

        plt.title('Todos Ordenados')
        plt.xlabel('Quantidade numeros')
        plt.ylabel('Tempo (em segundos)')
        
        plt.show()

        # para salvar em arquivo
        #plt.savefig('demo.png', bbox_inches='tight')


Main()