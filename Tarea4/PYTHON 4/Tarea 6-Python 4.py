lista1=0
lista2=0
x=1
while x<=5:
    valor=int(input("Introduce un valor de la lista 1:"))
    x=x+1
    lista1=lista1+valor
x=1
while x<=5:
    valor=int(input("Introduce un valor de la lista 2:"))
    x=x+1
    lista2=lista2+valor
if lista1>lista2:
    print("La lista 1 es mayor con un valor acumulado:",lista1)
else:
    if lista1<lista2:
        print("la lista 2 es mayor con un valor acumulado:",lista2)
    else:
        print("Ambas listas son iguales con un valor acumulado;",lista1)
    
