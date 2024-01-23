#funcion que crea una lista de n elementos
def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista?"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista

#Funcion que crea dos listas(positivos y negativos)
def dosListas(lista):
    positivos=[]
    negativos=[]
    for x in range(len(lista)):
        if lista[x]>=0:
            positivos.append(lista[x])
        else:
            negativos.append(lista[x])
    return [positivos,negativos]

def visualizar(positivos,negativos):
    print("Positivos:",positivos)
    print("Negativos:",negativos)

#Programa principal
lista=crealista()
print(lista)
positivos,negativos=dosListas(lista)
visualizar(positivos,negativos)
