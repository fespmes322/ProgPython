#Leer una lista de 5 empleados
def cargar_empleado():
    empleados=[]
    for x in range(5): 
        nombre=input("Introduce un nombre:")
        sueldo1=int(input("Introduce el primer sueldo:")
        sueldo2=int(input("Introduce el segundo sueldo:")
        sueldo3=int(input("Introduce el tercer sueldo:")
        empleado=[]
        empleado.append(nombre)
        empleado.append((sueldo1,sueldo2,suedo3))
    return empleados

#Visualizar el mayor sueldo de dos empleados
def visualizar(empleados):
    for empleados in empleados:
        total=0
        for sueldo in empleado[1]:
            total=total+sueldo
        print(empleado[0],"tiene un sueldo trimestral de ",total)
#Visualizar empleados con un mono trimestral mayor a 10000
def visualizarSuperior(empleados):
    print("Los empleados con un monto trimestral superior a 10000 son:")
    for empleados in empleados:
        total=0
        for sueldo in empleado[1]:
            total=total+sueldo
        if total>10000:
        print(empleado[0],"tiene un sueldo trimestral de ",total)
        
#Programa principal
empleados=cargar_empleados()
visualizar(empleados)
visualizarSuperior(empleados)
