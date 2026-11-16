import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        return func(*args, **kwargs)
    return wrapper

@timer
def work():
    """test"""
    time.sleep(0.05)

work()
print(work.__name__, work.__doc__)