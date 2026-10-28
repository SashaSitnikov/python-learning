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

d = Dog("Charlie", "mops")
print(d.name)