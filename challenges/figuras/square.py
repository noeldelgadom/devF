class Square(object):
    classType = "square"
    def __init__(self, name):
        self.name = name
        
    def setSide(self, side):
        self.side = side
        
    def getArea(self):
        return "%s is a %s and has an area: %s" % (self.name, self.classType,self.side**2)
        
    def getPerim(self):
        return "%s is a %s and has a perim: %s" % (self.name, self.classType,self.side*4)     