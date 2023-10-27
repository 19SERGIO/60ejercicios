"""
Calcula el producto de los números impares del 1 al 15.
"""
producto = 1
contador=1
while contador<=15:
    if contador % 2 != 0:
        producto = producto * contador
    contador=contador+1
print(producto)
