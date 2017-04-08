from triangle import Triangle
from circle import Circle
from square import Square
        
tri = Triangle("myTriangle")
tri.setSides(5,4,3)
print(tri.getArea())
print(tri.getPerim())

circ = Circle("myCircle")
circ.setRadius(4)
print(circ.getArea())
print(circ.getPerim())

sq  = Square("mySquare")
sq.setSide(3)
print(sq.getArea())
print(sq.getPerim())