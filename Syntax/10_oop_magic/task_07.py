class Multiplier:
    def __init__(self, n):
        self.n = n
        
    def __call__(self, x):
        return x * self.n
    

class Counter:
    def __init__(self):
        self.count = 0
        
    def __call__(self):
        self.count += 1
        return self.count

double = Multiplier(2)
numbers = [1, 2, 3, 4, 5]

result = list(map(double, numbers))
print(f"Результат работы map: {result}")

c = Counter()
print(f"Первый вызов счетчика: {c()}")
print(f"Второй вызов счетчика: {c()}")
print(f"Третий вызов счетчика: {c()}")

