#Input es la funcion que te permite guardar datos en una variable

#print("¿Cual es tu nombre?")
nom=input("¿Cuál es tu nombre?\t")

print("¿Cual es tu apellido paterno?")
ap=input()

print("Dame un primer numero")
a=input()

print("Dame un segundo numero")
b=input()
#Si no conviertes a int a y b no suma bien

#a=int(a)
#b=int(b)
suma=int(a)+int(b)

print("Tu nombre es {} {}.".format(nom,ap))
print("La suma de {} + {} es igual a {}".format(a,b,suma))