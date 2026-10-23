class InsufficientFundsError(Exception):
    """Недостаточно средств на счёте."""
    
class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError(f"Баланс не может быть меньше 0!")
        self.owner, self._balance = owner, balance
        self._history = []
        
    @property
    def balance(self):
        return self._balance
    
    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"
    
    def __str__(self):
        return f"Баланс: {self._balance}, История операций: {list(self._history)}"
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount
        self._history.append(f"Пополнение счета на сумму: {amount}")
        return self._balance
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self._balance < amount:
            raise InsufficientFundsError(f"Нужно {amount}, на счёте {self._balance}")
        self._balance -= amount
        self._history.append(f"Снятие со счета на сумму: {amount}")
        return self._balance
    
    
acc = BankAccount("Алекс", 1000)

acc.deposit(500)
print(acc)

try:
    acc2 = BankAccount("А", -500)
except ValueError as e:
    print(f"Поймали ошибку: {e}")
    
try:
    acc.deposit(-100)
except ValueError as e:
    print(f"Поймали ошибку: {e}")

try:
    acc.withdraw(-5)
except ValueError as e:
    print(f"Поймали ошибку: {e}")
    
try:
    acc.withdraw(5000)
except InsufficientFundsError as e:
    print(f"Поймали ошибку: {e}")

acc.withdraw(300)
print(acc)
