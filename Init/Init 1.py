class Persona:
    def _init_(self,nom,ed):
       self.nombre=nom
       self.edad=ed

    def imprimir(self):
        print("Datos de la persona:")
        print(self.nombre," tiene una edad de ",self.edad,"años")
        
    def mayorEdad(self):
        if (self.edad>=18):
            print("Es mayor de edad")
        else:
            print("no es mayor de edad")

#Principal
nom=input("Nombre de la persona:")
ed=int(input("Edad de la persona:"))
persona1=Persona(nom,ed)
persona1.imprimir()
persona1.mayorEdad()
