import copy
from contextlib import contextmanager

class InsufficientFundsError(Exception):
    """Недостаточно средств"""
    
class FakeDB:
    def __init__(self):
        self.data = {"a": 50, "b": 0}
        
@contextmanager
def transaction(db):
    new_db = copy.deepcopy(db.data)
    print("Начало")
    try:
        yield db
    except Exception:
        db.data = new_db
        print("Откат")
        raise
    else:
        print("Сохранено")
            
def transfer(db, src, dst, amount):
    if db.data[src] < amount:
        raise InsufficientFundsError("Недостаточно средств")
    
    db.data[src] -= amount
    db.data[dst] += amount
    
    print(f"Перевод со счета {src} на счет {dst} в размере {amount} рублей совершен успешно!")
            
db = FakeDB()

with transaction(db):
    transfer(db, "a", "b", 15)

print(db.data)

try:
    with transaction(db):
        transfer(db, "a", "b", 100)
except InsufficientFundsError as e:
    print(f"Возникла ошибка: {e}")

print(db.data)