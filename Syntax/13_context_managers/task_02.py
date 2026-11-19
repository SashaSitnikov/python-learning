import time


class Demo:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print(f"Вход: {self.name}")
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start

        print(f"Выход: {self.name}")
        print(f"Тип ошибки: {exc_type}")
        print(f"Прошло: {self.elapsed:.2f} с.")

        return False

with Demo("Test"):
    time.sleep(0.05)
