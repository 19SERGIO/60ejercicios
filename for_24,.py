"""
Calcula la suma de los dígitos de un número ingresado por el usuario, repitiendo el proceso 5 
veces.
"""
suma=0
for rango in range (5,0,-1):
    num=int(input("ingrese un numero: "))
    suma=suma+num
print(suma)