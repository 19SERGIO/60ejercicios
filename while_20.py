"""
calcula la suma de los números cuyos dígitos suman 7 del 1 al 100.
"""
suma = 0
i = 1
while i <= 100:
    if sum(int(digito) for digito in str(i)) == 7:
        suma += i
    i += 1
print(suma)


