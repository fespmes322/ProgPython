#funcion retorna el mayor de 2 numeros
def mayor(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2



#programa principal
n1=int(input("Introduce el valor 1:"))
n2=int(input("Introduce el valor 2:"))
n3=int(input("Introduce el valor 3:"))
n4=int(input("Introduce el valor 4:"))
print("El mayor de 4 valores es:",mayor(mayor(n1,n2),mayor(n3,n4)))
