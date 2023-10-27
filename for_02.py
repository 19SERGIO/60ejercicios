"""
. Calcula la suma de los números del 1 al 100.
"""
anterior=0
for i in range (1, 101, 1):
    
    print (i,"+", anterior,"= ",i+anterior)
    anterior=i
