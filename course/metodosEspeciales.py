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
        
    def __str__(self):
        return "Este es un objecto robot llamado %s" % self.name
        
    def __repr__(self):
        return "Robot(name=%s, lastname=%s)" % (self.name, self.lastname)
    
    def __del__(self):
        print("Objeto Destruido llamado %s" % self.name)
        
if __name__ == '__main__':
    robot = Robot("Edwin", "Salgado", 23, "hola")
    print(robot.__dict__)                           # Hace de un objecto un diccionario
    dic1 = robot.__dict__
    dic2 = robot.__dict__.copy()                    # dict2 es independiente
    print(dic1)
    print(dic2)
    
    #Después de modificarlos, modifico a robot, más no a dict2
    dic1['saludo'] = 'hello'
    print(robot.__dict__)
    print(dic1)
    print(dic2)
    
    # Probando la funcion __str__ 
    print(robot)
    
    # Probando la funcion __repr_
    print(repr(robot))