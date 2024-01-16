# Definir lista vacia
alumnos=[]
notas=[]
#Agregamos 4 nombres de alumnos y notas
for x in range(4):
    nombre=input("Introduce un alumno:")
    alumnos.append(nombre)
    nota=float(input("Introduce una nota:"))
    notas.append(nota)
#Visualizar las notas de alumnos
muybueno=0
for x in range(4):
    if notas[x]<4:
        print(alumnos[x],"Insuficiente")
    else:
        if notas[x]<=7:
            print(alumnos[x],"Bueno")
        else:
            muybueno=muybueno+1
            print(alumnos[x],"Muy bueno")
print("Alumnos muy bueno:",muybueno)
