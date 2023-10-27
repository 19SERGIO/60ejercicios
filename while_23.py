
"""
 Imprime los números que son primos gemelos en el rango del 1 al 100
"""
i = 2
while i < 101:
    es_primo_i = 1
    j = 2
    while j < i:
        if i % j == 0:
            es_primo_i = 0
            break
        j += 1
    if es_primo_i == 1:
        es_primo_i_mas_2 = 1
        j = 2
        while j < i + 2:
            if (i + 2) % j == 0:
                es_primo_i_mas_2 = 0
                break
            j += 1
        if es_primo_i_mas_2 == 1:
            print(i, i + 2)
    i += 1
