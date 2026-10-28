class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "голос"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return "гав"

class Cat(Animal):
    def speak(self):
        return "мяу"

d = Dog("Рекс", "лайка")
print(isinstance(d, Dog), isinstance(d, Animal), isinstance(d, Cat)) # True True False
print(type(d) is Animal, type(d) is Dog) # False True
print(issubclass(Dog, Animal), issubclass(Animal, Dog)) # True False
print(Dog.__mro__)




