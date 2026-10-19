def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Возраст должен быть целым числом!")
    if not 0 <= age <= 120:
        raise ValueError(f"Недопустимый возраст: {age}!")
    return age

try:
    print(set_age("20"))
except TypeError as e:
    print(f"Поймали ошибку: {type(e).__name__}: {e}")
try:
    print(set_age(-5))
except ValueError as e:
    print(f"Поймали ошибку: {type(e).__name__}: {e}")
try:
    print(set_age(25))
except (TypeError, ValueError) as e:
    print(f"Поймали ошибку: {type(e).__name__}: {e}")