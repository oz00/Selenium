inicio=0
fin=10

while(inicio <= fin):
    # Si no le damos el aumento esto se desborda
    inicio = inicio + 1
    if (inicio==5):
        continue
    print("Esto se repite " + str(inicio))