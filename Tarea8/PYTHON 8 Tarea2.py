oracion=input("Introduce una frase:")
vocales=0
frase=oracion.lower()
x=0
while x<len(frase):
    if frase[x]=='a' or frase[x]=='e' or frase[x]=='1' or frase[x]=='u' or frase[x]=='o':
        vocales=vocales+1
    x=x+1
print("Cantidad de vocales:",vocales)
