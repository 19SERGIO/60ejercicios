"""
 Imprime los números cuya suma de dígitos es un número primo en el rango del 1 al 100
"""
for num in range(1, 101):
    suma = sum(int(digito) for digito in str(num))
    if suma > 1:
        es_primo = True
        for i in range(2, suma):
            if suma % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)

