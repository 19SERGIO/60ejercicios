"""
Calcula la suma de los números que son palíndromos en el rango del 1 al 100.
"""
suma = 0
for num in range(1, 101):
    original = num
    reverso = 0
    while num > 0:
        digito = num % 10
        reverso = reverso * 10 + digito
        num = num // 10
    if original == reverso:
        suma =suma+ original
print(suma)
