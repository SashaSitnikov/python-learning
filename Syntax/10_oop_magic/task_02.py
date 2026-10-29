class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, k):
        if not isinstance(k, (int, float)):
            return NotImplemented
        return Vector(self.x * k, self.y * k)
    
    __rmul__ = __mul__
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)
    
    def __bool__(self):
        return self.x != 0 or self.y != 0
    
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v_zero = Vector(0, 0)

print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 2  = {v1 * 2}")
print(f"3 * v1  = {3 * v1}")
print(f"-v1     = {-v1}")
print(f"abs(v1) = {abs(v1)}")
print(f"v1 == v2: {v1 == v2}")
print(f"v1 истинен? {bool(v1)}")
print(f"v_zero истинен? {bool(v_zero)}")

try:
    result = v1 * v2
except TypeError as e:
    print(f"Поймали ошибку: {e}")