#Definir lista avcia
lista1=[]

#Agregamos 10 numeros a lista1
for x in range(10):
    valor=int(input("Introduce un nummero de la lista 1:"))
    lista1.append(valor)

#ordenamos la lista
for i in range(1,10):
    for j in range(10-i):
        if lista1[j]>lista1[j+1]:
            aux=lista1[j]
            lista1[j]=lista1[j+1]
            lista1[j+1]=aux
#Visualizamos la lista
print("La lista ordenada:",lista1)
