class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15°C)")
        self._celsius = value
        
    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
    
t = Temperature(25)
print(f"Цельсии: {t.celsius}°C")
print(f"Фаренгейты: {t.fahrenheit}°F")

try:
    t.celsius = -300
except ValueError as e:
    print(f"Поймали ошибку: {e}")

try:
    t.fahrenheit = 100
except AttributeError as e:
    print(f"Успешно поймали: {type(e).__name__}: {e}")

    




