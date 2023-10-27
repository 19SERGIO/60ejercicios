
"""
Calcula el promedio de los números pares del 1 al 50.
"""
num_pares = 0
suma = 0
promedio = 0
numeros = 1
while numeros < 51:
    if numeros % 2 == 0:
        num_pares = num_pares + 1
        suma = suma + numeros
    numeros += 1
promedio = suma / num_pares
print(promedio)