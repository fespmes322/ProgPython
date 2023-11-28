cantidad=0
n=int(input("Cuantos triangulos?"))
for x in range(n):
    base=float(input("base del triangulo:"))
    altura=float(input("altura del triangulo:"))
    superficie=base*altura/2
    print("El trangulo cuya base es ",base," y la altura",altura," tiene una superficie:",superficie)
    if superficie>12:
        cantidad=cantidad+1

print("Cantidad de triangulos cuya superficie es superior a 12:",cantidad)
