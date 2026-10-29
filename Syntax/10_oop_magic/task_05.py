class A:
    def __init__(self): print("A init")

class B(A):
    def __init__(self):
        print("B start"); print("B end")

class C(A):
    def __init__(self):
        print("C start"); super().__init__(); print("C end")

class D(C, B):
    def __init__(self):
        print("D start"); super().__init__(); print("D end")

D()