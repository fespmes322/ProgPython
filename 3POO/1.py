#Clase Socio con los campos nombre y antiguedad
class Socio:
    def _init_(self):
        self.nombre=input("Introduce nombre:")
        self.antiguedad=int(input("Introduce antiguedad:")

#VIsualizar un socio
    def imprimir(self):
        print(self.nombre," tiene una antiguedad en años de ",self.antiguedad)

#retornar antiguedad
    def verAntiguedad(self):
        return self.antiguedad

#Clase Club con una lista de socios
class Club:
    def _init_(self):
        self.socios=[]

#agregar un socio
    def agregarSocio(self):
        socio=Socio()
        self.socios.append(socio)

#Motrar todos los socios
    def mostrarSocios(self):
        for socio in self.socios:
            socio.imprimir()
#Mostrar un socio
    def mostrarUnSocio(self):
        pos=int(input("Introduce la posicion del socio a visualizar:"))
        if (pos<len(self.socio)):
            self.socios[pos].imprimir()
#Visualizar el socio de mayor antiguedad
    def mostrarMayorAntiguedad(self):
        mayor=self.socios[0]
        for socio in self.socios:
            if socio.verAntiguedad()>mayor.verAntiguedad():
                mayor=socio
        print("Socio de mayor antiguedad:")
        mayor.imprimir()
                   

#Principal
club=Club()
club.agregarSocio()
club.agregarSocio()
club.agregarSocio()
club.mostrarSocios()
club.mostrarUnSocio()
club.mostrarMayorAntiguedad()





