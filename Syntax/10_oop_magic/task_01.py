class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
a, b = Point(1, 2), Point(1, 2)
c, d = Point(3, 7), Point(12, 4)
print(a == b)
print(a is b)
print(a == (1, 2))
        
points = {c, d}
