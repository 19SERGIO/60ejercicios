"""
Calcula el promedio de los números pares del 1 al 50.
"""
num_pares=0
suma=0
promedio=0
for numeros in range(1,51,1):
    if numeros%2==0:
        num_pares=num_pares+1
        suma=suma+numeros
promedio=suma/num_pares
print(promedio) 