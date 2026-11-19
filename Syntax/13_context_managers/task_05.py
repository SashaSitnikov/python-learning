import time
from contextlib import contextmanager


@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter() - start:.2f} c")

try:
    with timer("работа"):
        time.sleep(0.05)
        raise ValueError("Тестовая ошибка")

except ValueError as e:
    print(f"Поймали ошибку: {e}")