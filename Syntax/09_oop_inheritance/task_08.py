class AppError(Exception):
    """Базовая ошибка приложения"""

class NotFoundError(AppError):
    """Пользователь не найден"""
    
class ValidationError(AppError):
    """Ошибка при проверке"""
    
def get_user(users, user_id):
    if not 0 <= user_id < len(users):
        raise NotFoundError(f"Пользователь {user_id} не найден")
    return users[user_id]

def validate_age(age):
    if 0 > age or age > 120:
        raise ValidationError(f"Некорректный возраст")
    return age

users = ["Alex", "Mia", "Vlad"]
try:
    validate_age(120)
except AppError as e:
    print(f"Нашли ошибку: {type(e).__name__}: {e}")
    
try: 
    validate_age(0)
except ValidationError as e:
    print(f"Нашли ошибку: {type(e).__name__}: {e}")

try:
    get_user(users, 4)
except Exception as e:
    print(f"Нашли ошибку: {type(e).__name__}: {e}")
except NotFoundError as e:
    print(f"Нашли ошибку: {type(e).__name__}: {e}")
