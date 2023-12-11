"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado.
Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa,
el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios.
"""
# Sumar 10 número
# Francisco Espinosa
# 11 de Diciembre del 2023
#Variable acumulativa, suma
suma=0
for x in range(10):
    num=int(input("Número:")) #Lectura del número
    suma=suma+num #acumulamos el número
#Visualizamos el total
print("La suma total es ",suma)
