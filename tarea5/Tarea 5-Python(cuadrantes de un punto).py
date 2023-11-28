primer=0
segundo=0
tercer=0
cuarto=0
n=int(input("Numero de coordenadas"))
for x in range(n):
    cordx=float(input("coordenada x:"))
    cordy=float(input("coordenada y:"))
    if cordx>0 and cordy>0:
        print("primer cuadrante")
        primer=primer+1
    else:
        if cordx<0 and cordy<0:
            print("tercer cuadrante")
            tercer=tercer+1
        else:
            if cordx>0 and cordy<0:
                print("Cuarto cuadrante")
                cuarto=cuarto+1
            else:
                print("segundo cuadrante")
                segundo=segundo+1
print("cantidad en primero cuadrante:",primer)
print("cantidad en segunda cuadrante:",segundo)
print("cantidad en tercera cuadrante:",tercer)
print("cantidad en cuarta cuadrante:",cuarto)
      
            

