"""
 Imprime los números que son múltiplos de 5 o 6 del 1 al 50.
"""
conta=1
while conta<=50:
    if conta%5==0 or conta%6==0:
        print(conta)
    conta+=1