#Al ocupar corchetes , se entiende que es un arreglo , separado por comas

nombres=["Yerik","Iker","Isabella","Nicky","Mimi"]

#COncatenando una posición de la lista nombres
print("Nombre seleccionado: "+nombres[0])
print("Nombre seleccionado: "+nombres[4])

#Sobre-escribir su valor e imprimir
nombres[4]="Kike"
print("Nombre seleccionado: "+nombres[4])

#Función para Agregar un nuevo valor a la lista
nombres.append("NUEVO")
print(nombres)