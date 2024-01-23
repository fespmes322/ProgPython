#funcion creamos una lista de articulos y de precios
def crearLista(n):
    articulos=[]
    precios=[]
    for x in range(n):
        articulo=int(input("Introduce el nombre del articulo:"))
        precio=int(input("Introduce el precio del articulo:"))
        articulos.append(articulo)
        precios.append(precio)
    return [articulos,precios]

#funcion visualizar los articulos y sus precios
def verSueldos(articulos,precios):
    for x in range(len(articulos)):
        print(articulos[x].":",precios[x])

#funcion articulo más caro
def articuloMasCaro(articulos,precios):
    masCaro=precios[0]
    pos=0
    for x in range(1,len(precios)):
        if precios[x]>masCaro:
            masCaro=precios[x]
    print("El articulo más caro es ",articulos[pos],"con precio de ",masCaro)

