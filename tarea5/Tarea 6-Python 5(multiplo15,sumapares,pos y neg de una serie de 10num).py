negativo=0
positivo=0
multiplos=0
sumapar=0
for x in range(10):
    num=int(input("Ingrese un numero:"))
    if num<0:
        negativo=negativo+1
    else:
            positivo=positivo+1
    if num%15==0:
        multiplos=multiplos+1
    if num%2==0:
        sumapar=sumapar+num
print("positivo:",positivo)
print("negativo:",negativo)
print("Multiplos de 15:",multiplos)
print("Suma de pares:",sumapar)
