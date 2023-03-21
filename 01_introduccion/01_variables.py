#01_introduccion a las variables de python
#lenguajes identados son los que te obligan a declarar de que tipo de variable es
#string, int, float
#Python no es un lenguaje identado
#Un programa se corre con Ctrl+shift+f10

#Variables numericas
a=100
b=50

suma=a+b
resta=a-b
multiplicacion=a*b
division=a/b

print("la suma es: "+str(suma))
print("la resta es: "+str(resta))
print("la multiplicación es: "+str(multiplicacion))
print("la división es: "+str(division))

#Variables de texto
nombre="Isamara"
ap="Espinosa"
am="Alvarez"

print("Mi nombre es "+nombre+" "+ap+" "+am)

#Variable boolen
encendido=True

#Con Python pordemos hacer que nos diga que tipo de variable es alguna variable
print(type(encendido))