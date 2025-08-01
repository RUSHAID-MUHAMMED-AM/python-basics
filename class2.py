# find circumference and area of the circle
# area=pi*r*r
# circumference=2*pi*r

class Circle:
    pi=3.14
    def __init__(self,r):
         self.r=r
    def get_circumference(self):
        return 2*Circle.pi*self.r
    def get_area(self):
        return Circle.pi*self.r*self.r
        
circle_1=Circle(5)
print(circle_1.get_circumference())
print(circle_1.get_area())