# Definir lista vacia
lista1=[]
lista2=[]
lista3=[]
#Agregamos 4 numeros a lista1 y lista2
for x in range(4):
    valor=int(input("Introduce un numero de la lista 1:"))
    lista1.append(valor)
    valor=int(input("Introduce un numero de lista 2:"))
    lista2.append(valor)
#sumar ambas listas
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)
#Visualizar lista suma
    print("La lista resultante:",lista3)
