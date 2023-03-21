#Cadenas simples
texto="Hola bienvenidos a python"
print(texto)

#Como imprimimos solo una parte de la cadena de texto
print(texto[3])
print(texto[5:15])
print(texto[5:])
print(texto[-6:])

#Funciones de cadenas
nombre="Juan"
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())

#Imprimir una string en modo de arreglo
cadena="ruby,java,selenium,javascript"
print(cadena)
print(cadena.split(','))

#Imprimir cadena con la funcion format
nom="Yerik Alejandro"
ap="Miranda"
am="Silva"
edad= 8


print("El nombre es {} el apellido paterno es {} el apellido materno es {}.".format(nom,ap,am))

print("El nombre es: "+nom+" el apellido paterno es: "+ap+" el apellido materno es: "+am)

print("El nombre es: "+nom+" la edad es: "+str(edad))
print("El nombre es {} y la edad es {}.".format(nom,edad))

