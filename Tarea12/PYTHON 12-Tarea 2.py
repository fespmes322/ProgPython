#función que crea una lista de n elementos
def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista?"))
    for x in range(n):
        valor=int(input("Introduce un lemento de la lista:"))
        lista.append(valor)
    return lista

#funcion que devuelve la palabra con mas caracteres de la lista
def mascaracteres(lista):
    palabra=lista[0]
    for x in range(1,len(lista)):
        if len(lista[x])>len(palabra):
            palabra=lista[x]
    return palabra


#programa principal
palabras=crearLista()
print(palabras)
print("palabra con mas caracteres:",mascaracteres(palabras))
