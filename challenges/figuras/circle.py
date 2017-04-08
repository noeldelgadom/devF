class Circle(object):
    classType = "circle"
    def __init__(self, name):
        self.name = name
        
    def setRadius(self, radius):
        self.radius = radius
        
    def getArea(self):
        return "%s is a %s and has an area: %s" % (self.name, self.classType,3.1416*self.radius**2)
        
    def getPerim(self):
        return "%s is a %s and has a perim: %s" % (self.name, self.classType,3.1416*self.radius*2)