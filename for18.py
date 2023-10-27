"""
 Calcula el producto de los números pares del 1 al 20.

"""
producto = 1
for i in range(2, 21, 2):
    producto *= i
print(producto)
