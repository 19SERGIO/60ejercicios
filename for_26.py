"""
Calcula el producto de los números impares del 1 al 15.
"""
producto = 1
for i in range(1, 16):
    if i % 2 != 0:
        producto = producto * i
print(producto)
