class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Гав"

class Cat(Animal):
    def speak(self):
        return "Мяу"
    
class Robot:
    def speak(self):
        return "Бип"
    
def make_noise(obj):
    print(obj.speak())
    
make_noise(Dog("Шарик"))
make_noise(Cat("Мурка"))
make_noise(Robot())

try:
    make_noise(42)
except AttributeError as e:
    print(f"\nПоймали ошибку: {type(e).__name__}: {e}")

