import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Прошло {self.elapsed:.2f} c")
        return False
    
t = Timer()

try:
    with t:
        time.sleep(0.5)
        raise ValueError("Тестовая ошибка")
except ValueError as e:
    print(f"Поймали ошибку: {e}")

print(f"Время из атрибута: {t.elapsed:.2f} с")
