import time
from functools import wraps


class AccessDeniedError(Exception):
    "Недостаточно прав"
    
def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise AccessDeniedError(f"Нужна роль {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__}: {time.perf_counter() - start:.3f} c")
    return wrapper

@timer
@require_role("Admin")
def delete_user(user, user_id):
    return f"Пользователь {user_id} удалён"

print(delete_user("Admin", 4))
print(delete_user("User", 12))