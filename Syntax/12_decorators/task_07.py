from functools import wraps

def retry(attempts=3, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Попытка {attempt} не удалась: {e}")
                    if attempt == attempts:
                        raise
        return wrapper
    return decorator

@retry(3, ValueError)
def operation(a, b):
    return a + b

print(operation(123, "dd"))