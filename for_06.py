"""
 Calcula la suma de los números múltiplos de 3 del 1 al 50.
"""
suma=0
for i in range (1,51,1):
    if i%3==0:
        print(i)
        suma= suma+i

print("la suma es igual a ", suma)