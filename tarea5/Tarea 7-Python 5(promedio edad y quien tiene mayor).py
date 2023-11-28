mañana=0
tarde=0
noche=0
print("Turno de mañana:")
for x in range(5):
    edad=int(input("Edad:"))
    mañana=mañana+1
print("Turno de tarde:")
for x in range(6):
    edad=int(input("Edad:"))
    tarde=tarde+1
print("Turno de noche:")
for x in range(11):
    edad=int(input("Edad:"))
    noche=noche+1
promedio1=mañana/5
promedio2=tarde/6
promedio3=noche/11
print("Edad medio de la mañana:",promedio1)
print("edad medio de la tarde:",promedio2)
print("edad medio de la noche:",pormedio3)
if promedio1>promedio2 and promedio1>promedio3:
    print("El turno de mañana tiene mas promedio de edad")
else:
    if promedio2>promedio3:
        print("El turno de tarde tiene mayor promedio de edad")
    else:
        print("El turno de noche tiene mayor promedio de edad")

    
