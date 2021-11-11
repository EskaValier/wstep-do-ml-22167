# -*- coding: utf-8 -*-
import numpy
"""
Created on Mon Nov  8 14:06:23 2021

@author: dsocz
"""
# %% tablica 10-ciu 0
table1 = []
for i in range(0, 10):
    table1.append(0)
    pass

# %% tablica 10-ciu 5-tek
table2 = []
for i in range(0, 10):
    table2.append(5)
    pass

# %% tablica liczb z przedziału 10-50
table3 = []
for i in range(10, 51):
    table3.append(i)
    pass

# %% tablica 3x3 zawierająca liczby 0-8
table4 = []
table4help = []
for i in range(0, 3):
    table4help = []
    for j in range(0, 3):
        table4help.append(i*3+j)
        pass
    table4.append(table4help)
    pass

# %% macierz jednostkowa 3x3
table5 = []
table5help = []
for i in range(0, 3):
    table5help = []
    for j in range(0, 3):
        if i==j:
            table5help.append(1)
        else:
            table5help.append(0)
        pass
    table5.append(table5help)
    pass

# %% macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej
normalVal = numpy.random.normal(0,10,25)
table6 = []
table6help = []
for i in range(0, 5):
    table6help = []
    for j in range(0, 5):
        table6help.append(normalVal[i*5+j])
        pass
    table6.append(table6help)
    pass

# %% macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01
table7 = []
table7help = []
for i in range(0, 10):
    table7help = []
    for j in range(1, 11):
        table7help.append((i*10+j)/100)
        pass
    table7.append(table7help)
    pass

# %% tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1
table8 = []
for i in range(0, 21):
    table8.append(1/20*i)
    pass

# %% tablicę zawierającą losowe liczby z przedziału (1, 25)
from random import randint
table9 = []
for i in range(0, 25):
    table9.append(randint(1,25))
    pass

# %% zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami
table10 = []
for i in range(0, 5):
    table10.append(table9[i*5:i*5+5])
    pass

# %% suma, srednia, suma kolumn
table10sumAll = 0
table10Column = [0,0,0,0,0]
for i in range(0, 5):
    for j in range(0, 5):
        table10sumAll = table10sumAll + table10[i][j]
        table10Column[j] = table10Column[j] + table10[i][j]
        pass
    pass
table10Average = table10sumAll/25

# %% dewiacja
import math
sumAll = 0
for i in range(0, 5):
    for j in range(0, 5):
        sumAll = sumAll + pow(table10[i][j] - table10Average, 2)
        pass
    pass
table10Deviation = math.sqrt(sumAll/25)

# %% macierz 5X5 z losowych liczb 0-100
table11 = []
for i in range(0, 5):
    table11help = []
    for j in range(0, 5):
        table11help.append(randint(0,100)) 
        pass
    table11.append(table11help)
    pass

# %%mediana, min, max
table11mediana = numpy.median(table11)
table11min = numpy.min(table11)
table11max = numpy.max(table11)

# %% transpozycja
table12 = []
for i in range(0, 5):
    table12help = []
    for j in range(0, 7):
        table12help.append(randint(0,100)) 
        pass
    table12.append(table12help)
    pass
table12transpozition = numpy.swapaxes(table12, 1, 0)

# %% dodawanie macierzy
table13a = []
table13b = []
for i in range(0, 5):
    table13Ahelp = []
    table13Bhelp = []
    for j in range(0, 5):
        table13Ahelp.append(randint(0,100)) 
        table13Bhelp.append(randint(0,100)) 
        pass
    table13a.append(table13Ahelp)
    table13b.append(table13Bhelp)
    pass

table13sum = numpy.add(table13a, table13b)

# %% mnozenie macierzy
table14a = []
for i in range(0, 3):
    table14ahelp = []
    for j in range(0, 3):
        table14ahelp.append(randint(0,100)) 
        pass
    table14a.append(table14ahelp)
    pass

table14b = []
for i in range(0, 9):
    table14bhelp = []
    for j in range(0, 9):
        table14bhelp.append(randint(0,100)) 
        pass
    table14b.append(table14bhelp)
    pass

table14matmul = numpy.matmul(table14a, table14b)
table14multiply = numpy.multiply(table14a, table14b)