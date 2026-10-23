class Dog:
    def __init__(self, name, age):
        self.name, self.age = name, age
        
    def bark(self):
        return f"Привет, я {self.name}, мне {self.age} лет"
    

d1 = Dog("Марс", 10)
d2 = Dog("Брист", 5)

print(d1.bark())
print(Dog.bark(d1))

