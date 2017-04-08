from Vehicle import Vehicle

class Car(Vehicle)
      def __init__(self,color,precio,combustible):
          super().__init__(color,precio,combustible)
          self.placas = placas
          self.caballos = caballos
          self.num_puertas = num_puertas

    print("Estoy en car")
    print("Este es main")


if __name__ == '__main__':
    car = Car("Rojo","12121212121","V8","Dissel","345ert")
    print(car.moverse())
    print(car.precio)
    print(car.muestraTipo("Deportivo"))
