from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Имя: {func.__name__}, Аргументы: {args}, {kwargs}, Результат: {result}")
        return result
    return wrapper

@log_calls
def add(a, b=0):
    return a + b

print(add(5, b=4))