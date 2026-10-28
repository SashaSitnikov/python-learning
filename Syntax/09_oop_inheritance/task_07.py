class Engine:
    def __init__(self, running=False):
        self.running = running
    
    def start(self):
        self.running = True
        return "Двигатель запущен!"
    
    def stop(self):
        self.running = False
        return "Двигатель заглушен!"
    

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()
        
    def __repr__(self):
        return f"Car(model={self.model!r}, running={self.engine.running})"
        
    def drive(self):
        if not self.engine.running:
            action = self.engine.start()
            return f"{self.model}: {action} Поехали!"
        else:
            return f"{self.model}: Двигатель уже работал. Поехали!"

my_car = Car("Toyota")
print(my_car.drive())