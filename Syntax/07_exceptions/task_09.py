class InsufficientFundsError(Exception):
    """Недостаточно средств на счете"""
    
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    if amount > balance:
        raise InsufficientFundsError(f"Нужно {amount}, на счете {balance}")
    return balance - amount
    
try:
    print(withdraw(1000, 0))
except ValueError as e:
    print(f"Ошибка: {e}")
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")
    
try:
    print(withdraw(1000, 1500))
except ValueError as e:
    print(f"Ошибка: {e}")
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")
    
try:
    print(withdraw(1000, 500))
except ValueError as e:
    print(f"Ошибка: {e}")
except InsufficientFundsError as e:
    print(f"Ошибка: {e}")