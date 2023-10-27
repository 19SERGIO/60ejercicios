"""
 Imprime los números cuya suma de dígitos es un número primo en el rango del 1 al 100
"""
num = 1
while num <= 100:
    suma = sum(int(digito) for digito in str(num))
    if suma > 1:
        es_primo = True
        i = 2
        while i < suma:
            if suma % i == 0:
                es_primo = False
                break
            i += 1
        if es_primo:
            print(num)
    num += 1
