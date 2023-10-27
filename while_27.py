"""
Imprime los números que son múltiplos de 3 y 5 del 1 al 50.
"""
num=1
while num<=50:
    if num%3==0 and num%5==0:
        print(num)
    num=num+1