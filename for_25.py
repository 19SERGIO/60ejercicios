"""
 Imprime una serie de caracteres ingresados por el usuario uno por uno, en orden inverso.
"""
texto = input("Ingresa una serie de caracteres: ")
for i in texto[::-1]:
    print(i)