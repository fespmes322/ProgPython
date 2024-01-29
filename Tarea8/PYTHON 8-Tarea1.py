oracion=input("Introduce una oracion:")
palabras=1
longitud=len(oracion)
x=0
while x<longitud:
    if(oracion[x]==" "):
        palabras=palabras+1
    x=x+1
print("Palabras:",palabras)
