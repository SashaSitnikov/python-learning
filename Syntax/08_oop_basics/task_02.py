class Rectangle:
    def __init__(self, width, height):
        self.width, self.height = width, height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def __str__(self):
        return f"Прямоугольник {self.width}x{self.height}"

rect = Rectangle(3, 4)
print(rect)