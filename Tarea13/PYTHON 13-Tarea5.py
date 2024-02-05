#Craera una lista de la forma [("Hola",4),("mundo",5)...
def cargar_palabras():
    palabras=[]
    longitud=1;
    while longitud>0:
        palabra=input("Introduce una palabra:")
        longitud=len(palabra)
        palabras.append((palabra,longitud))
    return palabras

#Visualizar palabras de más de 5 caracteres
def visualizar_palabras(palabras):
    for palabra in palabras:
        totalVotos=0
        if palabra[1]>5:
            print(palabra[0])

#Programa principal
palabras=cargar_palabras()
visualizar_palabras(palabras)
