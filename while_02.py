"""
. Calcula la suma de los números del 1 al 100.

"""
num=1
anterior=0
while num<=100:
    print(num,"+", anterior,"=", num+anterior)
    anterior=num
    num=num+1