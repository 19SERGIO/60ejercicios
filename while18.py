"""
 Calcula el producto de los números pares del 1 al 20.

"""

producto = 1
i = 2
while i <= 20:
    if i % 2 == 0:
        producto *= i
    i += 1
print(producto)

