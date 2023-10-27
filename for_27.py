"""
 Imprime los números que son múltiplos de 3 y 5 del 1 al 50.
"""
for k in range(1, 51, 1):
    if k % 3 ==0 and k%5==0:
        print(k)