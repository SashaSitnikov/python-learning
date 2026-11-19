import time
from contextlib import suppress


class Ignore:
    def __init__(self, *exceptions):
        self.exceptions = exceptions
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc, tb):
        return exc_type is not None and issubclass(exc_type, self.exceptions)
    
with Ignore(KeyError):
    {}["x"]
print("дошли")

with Ignore(ValueError):
    num = int("abc")
print("дошли")


with suppress(ValueError):
    num = int("sdf")
print("дошли")
