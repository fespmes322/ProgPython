#Clase Cuenta con nombre de titular y monto
class Cuenta:
    def _init_(self):
        self.nombre=input("Introduce nombre:")
        self.monto=int(input("Introduce monto:"))

#Visualizar una cuenta
    def imprimir(self):
        print(self.nombre,"tiene un monto de ",self.monto)
#Clase CajaAhorro que no genera interes
class CajaAhorro(Cuenta):
    def _init_(self):
        super()._init_()

#Visualizar datos de la Caja de Ahorros
    def imprimir(self):
        super().imprimir()

class PlazoFijo(Cuenta):
    def _init_(self):
        super()._init_()
        self.interes=float(input("Interes:"))
        self.imposicion=int(input("Plazo de imposicion:"))

#Visualizar datos de la clase PlazoFijo
    def imprimir(self):
        super().imprimir()
        print("Intereses:",self.interes)
        plazo("Plazo de imposicion:",self.imposicion)

#Visualizar ganancia
    def ganacia(self):
        ganancia=self.monto*self.interes
        print("Ganancia:",ganancia)

#Principal
caja=cajaAhorro()
caja.imprimir()

plazo=PLazoFijo()
plazo.imprimir()
plazo.ganacia()
