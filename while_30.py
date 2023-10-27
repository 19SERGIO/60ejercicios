"""
 Calcula la suma de los números que son divisibles por 3 o 7 en el rango del 1 al 50.
"""
num=1
suma=0
while num<=50:
    if num%3==0 or num%7==0:
        suma=num+suma
    num=num+1