#Bucles, ciclos
#Saber si todos los estudiantes les quedó claro el tema, y no repetir la pregunta n veces


#Ejemplo for con arreglo
nums =[0,1,2,3,4,5]
for n in nums:
    print(n)
#Imprimir de forma manual
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])
print(nums[5])

#Ejemplo For rango,
#Utiliza para enteros y se indica en donde va a parar
for x in range(10):
    print("Python")
    #Finaliza en posición #10 [0-9]
    print("Python "+str(x))

#COmbinar código bucle + if , donde se rompa en cierto valor
coleccion = [2,4,6,8,10,12,14]
for e in coleccion:
    if e==8:
        break
    print(e)

#COmbinar código bucle + if , donde se omita cierto valor (continue)
coleccion = [2,4,6,8,10,12,14]
for e in coleccion:
    if e==8:
        continue
    print(e)


#Ejemplo 2
colores=["rojo","verde","amarillo"]
print(colores[0])
print(colores[1])
print(colores[2])
#¿Que pasa si son 100 colores?
for x in colores:
    print(x)

#Tambien sirve con cadenas
nombre="Silvia Orozco Rodriguez"
for x in nombre:
    print(x)

#Rangos
for x in range(10,20):
    print(x)

#incrementos
for x in range(10,20,5):
    print(x)

#Romper ciclos
for x in range(0,100,7):
    if(x >=75):
        break
    print(x)

#Continuar ciclos
for x in range(1,11):
    if(x==3 or x==6):
        continue
    print(x)

#While
#La diferencia con for es que en while podemos decir que pare hasta que algo ocurra
inicio=1
fin=10

while(inicio <= fin):
    # Si no le damos el aumento esto se desborda
    inicio = inicio + 1
    print("Esto se repite "+str(inicio))

while(inicio <= fin):
    # Si no le damos el aumento esto se desborda
    inicio = inicio + 1
    if (inicio==5):
        break
    print("Esto se repite "+str(inicio))

while(inicio <= fin):
    # Si no le damos el aumento esto se desborda
    inicio = inicio + 1
    if (inicio==5):
        continue
    print("Esto se repite " + str(inicio))

#Ejercicio: Indicar los número del 1 al 7 sin agregar 3
#Imprimir n en cada vuelta
#Si n es 3, break
#Si no entonces muestra: "No se encontro el #3"
numeros = [1,2,3,4,5,6,7]
for n in numeros:
    if n==3:
        print('No se encontró el número 3')
        break
    print(n)







