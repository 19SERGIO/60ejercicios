"""
 Imprime los números que son múltiplos de 5 o 6 del 1 al 50.
"""
for k in range(1,51,1):
    if k%5==0 or k%6==0:
        print(k)