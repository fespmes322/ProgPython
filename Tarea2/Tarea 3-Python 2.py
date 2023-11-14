num1=int(input("Introduce un numero de uno o dos digitos "))
if num1>0:
    if num1<100:
        if num1>=10:
            print("El numero tiene dos cifras")
        else:
            print("El numero tiene una cifra")
    else:
        print("El numero tiene mas de dos cifras")
else:
    print("El numero es negativo")
        



    
