# Definir lista vacia
productos=[]
precios=[]
#Agregamos 5 nombres de productos y precio
for x in range(5):
    producto=input("Introduce un producto:")
    productos.append(producto)
    precio=float(input("Introduce un precio:"))
    precios.append(precio)
#Visualizar los productos superior al primero
print("El precio del primer producto, ",productos[0],"es",precios[0])
print("Los productos con precio superior son:")
for x in range(1,5):
    if (precios[x]>precios[0]):
        print(productos[x],"",precios[x])
