"""
calcula la suma de los números cuyos dígitos suman 7 del 1 al 100.
"""
suma = 0
for i in range(1, 101):
    if sum(int(digito) for digito in str(i)) == 7:
        suma += i
print(suma)

