#Condicionales: SI /NO
#importante : Estructura, dos puntos y sangría
a=100
b=500
c=120

if(a>b):
    print("El mayor es a "+str(a))

if(a<b or a>c):
    print("{} es menor que {} ó {} es mayor que {}".format(a,b,a,c))
    print("{}<{} ó {}".format(a,b,a,c))

#Para python es muy importante respetar el tabulador de los dos puntos de if
#Ejemplo fail
#if(a>b):
#print ("prueba")

#Uso del else, no se cumple la primera condición
if(a>b):
    print("El mayor es a "+str(a))
else:
    print("El mayor es b "+str(b))

#Condicionar nombres
nom = "Cupido"
if (nom == "Cupido"):
    print("Eres el sobrino menor de la instructora")
else:
    print("Tu no eres el Cupidin")

#Funciones y condicionales
nom = "YerIk"
if(nom.lower()=="yerik"):
    print("Nombre yerik en minusculas")
else:
    print("Nombre yerik mayusculas {}".format(nom.upper()))

#Elif
a=4
b=4
c=4

#Ejemplo con sintaxis incorrecta de if anidados

# if(a>b):
#     if(a>c):
#         print("El mayor es a "+str(a))

if(a>b and a>c):
    print("El numero mayor es A")
elif(b>a and b>c):
    print("El numero mayor es B")
elif (c > a and c > c):
    print("El numero mayor es C")
else:
    print("Ninguna se cumple")

#ejemplo con if anidador y con OR
a=100
b=500
c=120

if(a<b or a>c):
    print("{} es menor que {} ó {} es mayor que {}".format(a,b,a,c))
    print("{} < {} ó {} >  {}".format(a, b, a, c))

#ejemplo con if y not
if not(a>b):
    print("EJEMPLO NOT: {} NO es mayor que {} ".format(a, b))

#ejemplo input con if
print("¿Dudas sobre condicionales?")
respuesta=input()

if (respuesta== "no"):
    print("Continuar con el tema de Bucles")
else:
    print("Vuelve a explicar el tema de condicionales")
