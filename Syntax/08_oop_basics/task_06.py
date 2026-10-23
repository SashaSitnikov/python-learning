class User:
    def __init__(self, name, age):
        self.name, self.age = name, age
        
    def greet(self):
        return f"Привет меня зовут {self.name}"
    
    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name.strip(), int(age))
    
    @staticmethod
    def is_adult(age):
        return age >= 18

u = User.from_string("Alex,20")
print(u.greet(), User.is_adult(u.age))