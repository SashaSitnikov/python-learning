class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return "голос"

class Dog(Animal):
    def speak(self):
        return "гав"

class Cat(Animal):
    def speak(self):
        return "мяу"

animals = [Dog("Dog"), Cat("Cat"), Animal("Animal")]
for a in animals:
    print(f"{a.speak()} - {a.name}")