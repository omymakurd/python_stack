class Shape:
    
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14159 * ((self.radius)*(self.radius))
    def perimeter(self,):
        return 2*3.14159*self.radius
class Triangle(Shape):
    def __init__(self,base,height,a,b,c):
        self.base=base
        self.height=height
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        return self.a+self.b+self.c
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4* self.side
circle1=Circle(20)
print(circle1.area()) 
print(circle1.perimeter())
triangl1=Triangle(20,30,10,20,30)
print(triangl1.area()) 
print(triangl1.perimeter()) 
square1=Square(10)
print(square1.area())
print(square1.perimeter())