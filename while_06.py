"""
Calcula la suma de los números múltiplos de 3 del 1 al 50
"""
num=1
suma=0
while num<=50:
    if num%3==0:
        print(num)
        suma=suma+num
    num=num+1
print("la suma es igual a ", suma)

