class Vehicle:
    def __init__(self,color,precio,motor,combustible):
        self.color = color
        self.precio = precio
        self.motor = motor
        self.combustible = combustible

    def moverse(self):
        return "Moviendose"

    def recargarse(self):
        return "tanque lleno"

class Transport:

    def __init__(self,tipo="Familiar"):
        self.tipo = tipo

    def muestraTipo(self,tipo):
        return "Mi tipo es %s" % tipo          
