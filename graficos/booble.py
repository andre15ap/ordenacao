# coding: utf-8

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


class Main:
    def __init__(self):
        dataset = open('../saidas/buble_aleatorio.csv', 'r')
        x = []
        y = []
        for line in dataset:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset.close()
        plt.plot(x, y, label='Aleatórios')

        dataset2 = open('../saidas/buble_inverso.csv', 'r')
        x = []
        y = []
        for line in dataset2:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset2.close()
        plt.plot(x, y, label='invertidos')

        dataset3 = open('../saidas/buble_ordenado.csv', 'r')
        x = []
        y = []
        for line in dataset3:
            line.strip()
            valor_x, valor_y = line.split('\t')
            valor_y = float(valor_y.replace('\n',''))
            x.append(valor_x)
            y.append(valor_y)
        
        dataset2.close()
        plt.plot(x, y, label='Ordenados')


        plt.legend()
        plt.grid(True)

        plt.title('Booble Sort com valores Ordenados, Aleatórios e Invertidos')
        plt.xlabel('Quantidade numeros')
        plt.ylabel('Tempo (em segundos)')
        
        plt.show()

        # para salvar em arquivo
        #plt.savefig('demo.png', bbox_inches='tight')


Main()