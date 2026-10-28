from abc import ABC, abstractmethod
from math import pi, sin

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Площадь фигуры"""
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return (self.radius ** 2) * pi
        
    
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h 
        
    def area(self):
        return self.w * self.h
    
class Triangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def area(self):
        return 0.5 * self.a * self.b
        
lst = [Circle(14), Rectangle(8, 4), Triangle(10, 15)]

total_s = sum(el.area() for el in lst)
print(total_s)