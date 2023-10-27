"""
 Calcula la suma de los números que son divisibles por 3 o 7 en el rango del 1 al 50.
"""
suma=0
for k in range(1,51,1):
    if k %3==0 or k%7==0:
        suma=suma+k
print(suma)