"""
 Imprime una serie de caracteres ingresados por el usuario uno por uno, en orden inverso.
"""
texto = input("Ingresa una serie de caracteres: ")
i = len(texto) - 1
while i >= 0:
    print(texto[i])
    i = i -1

