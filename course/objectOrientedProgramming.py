class Robot:
    def __init__(self, name, lastname, age, password):
        self.name = name                            # Un atributo
        self.lastname = lastname                    # Otro atributo
        self._age = age                             # Atributo protegido
        self.__password = password                  # Atributo privado
    
    def getAge(self):
        return self._age
        
    def setAge(self, age):
        self_age = age
        
    def saluda(self):
        print("Hola, soy %s" % self.name)

r1 = Robot("Pedro","Salgado",30,"hola")
print(r1.name, r1.lastname)
r1.name = "Paco"
print(r1.name)
print(r1._age)
r1._age = 42
print(r1._age)
print(r1.saluda())
#print(r1.__password)                # Este no se puede print por ser privado
print("-------")

class Vehicle:
    def __init__(self, color, precio, motor, combustible):
        self.color = color
        self.precio = precio
        self.motor = motor
        self.combustible = combustible
        
    def moverse(self):
        return "Me estoy moviendo"
    def recargarCombustible(self):
        return "Tengo tanque lleno"
        
class Transport:
    def __init__(self, tipo=None):
        self.tipo = tipo
        
    def muestraTipo(self):
        return "Mi tipo es : %s" % self.tipo
        
        
class Car(Vehicle):
    def __init__(self, color, precio, motor, combustible, placas, caballos, num_puertas):
        super().__init__(color, precio, motor, combustible)
        self.placas = placas
        self.caballos = caballos
        self.num_puertas = num_puertas
        
if __name__ == '__main__':
    car = Car("rojo",20899,"V8","diesel","f7jd8",200,2)
    print(car.moverse())
    print(car.precio)
    print(car.muestraTipo())