import time


class Demo:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Вход: {self.name}")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"Выход: {self.name}, прошло {self.elapsed:.2f} с")
        return False

with Demo("A") as a, Demo("B") as b:
    print("go")
    
with Demo("A") as a:
    with Demo("B") as b:
        print("go")
