"""
 Imprime los números que son primos gemelos en el rango del 1 al 100
"""
for i in range(2, 101):
    es_primo_i = 1
    for j in range(2, i):
        if i % j == 0:
            es_primo_i = 0
            break
    if es_primo_i == 1:
        es_primo_i_mas_2 = 1
        for j in range(2, i + 2):
            if (i + 2) % j == 0:
                es_primo_i_mas_2 = 0
                break
        if es_primo_i_mas_2 == 1:
            print(i, i + 2)
