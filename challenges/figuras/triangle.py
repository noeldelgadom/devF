class Triangle(object):
    classType = "triangle"
    def __init__(self, name):
        self.name = name
        
    def setSides(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def getArea(self):
        return "%s is a %s and has an area: %s" % (self.name, self.classType,self.side1 * self.side2 / 2)
    
    def getPerim(self):
        return "%s is a %s and has a perim: %s" % (self.name, self.classType,self.side1 + self.side2 + self.side3)