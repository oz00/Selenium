#Operadores de comparación
#Importante mencionar la diferencia entre = y ==
a=10
b=11
c=5
print("¿Los numeros {} y {} son iguales? ".format(a,b)+str(a==b))
x=1
y=1
print("¿Los numeros {} y {} son iguales? ".format(x,y)+str(x==y))

#operador mayor que y menos que
print("¿El numero {} en mayor que el numero {} ? ".format(a,b)+str(a>b))
print("¿El numero {} en mayor que el numero {} ? ".format(b,a)+str(b>a))

print("¿El numero {} en mayor que el numero {} ? ".format(a,b)+str(a<b))
print("¿El numero {} en mayor que el numero {} ? ".format(b,a)+str(b<a))

print("¿El numero {} en mayor o igual que el numero {} ? ".format(x,y)+str(x<=y))
print("¿El numero {} en menor o igual que el numero {} ? ".format(x,y)+str(x>=y))

print("¿El numero {} es diferente a el numero {} ? ".format(a,b)+str(a!=b))
print("¿El numero {} es diferente a el numero {} ? ".format(x,y)+str(x!=y))

#Funciones and y or (operadores)
a<b and a<c
print("Si a es menor que b y a es menor que c: "+str(a<b and a<c))
print("Si a es menor que b y a es menor que c: "+str(a<b or a<c))



