from functools import wraps

routes = {}

class AccessDeniedError(Exception):
    """Недостаточно прав."""


def route(path, method="GET"):
    def decorator(func):
        routes[(method, path)] = func
        return func
    return decorator


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[log] {func.__name__}(args={args}, kwargs={kwargs}) -> {result!r}")
        return result
    return wrapper


def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") != role:
                raise AccessDeniedError(f"Нужна роль {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator


@route("/hello")
def hello(name="мир"):
    return f"Привет, {name}!"


@route("/sum")
@log_calls
def add(a, b):
    return a + b


@route("/admin")
@require_role("admin")
def admin_panel(user):
    return f"Добро пожаловать, {user['name']}"


@log_calls
@route("/sum-wrong")
def add_wrong(a, b):
    return a + b


def handle(method, path, **params):
    handler = routes.get((method, path))
    if handler is None:
        return "404 Not Found"
    try:
        return handler(**params)
    except AccessDeniedError:
        return "403 Forbidden"


if __name__ == "__main__":
    print(handle("GET", "/hello", name="Аня"))
    print(handle("GET", "/hello"))
    print(handle("GET", "/sum", a=2, b=3))
    print(handle("GET", "/sum-wrong", a=2, b=3))
    print(handle("GET", "/nope"))
    print(handle("POST", "/hello"))
    print(handle("GET", "/admin", user={"name": "Аня", "role": "admin"}))
    print(handle("GET", "/admin", user={"name": "Олег", "role": "user"}))