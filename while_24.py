"""
Calcula la suma de los dígitos de un número ingresado por el usuario, repitiendo el proceso 5 
veces.
"""
suma=0
rango=5
while rango>0:
    num=int(input("ingrese un numero: "))
    suma=suma+num
    rango=rango-1
print(suma)