from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @abstractmethod
    def foo(self): pass

A()  # raises TypeError

class B(A):
    pass

B()  # raises TypeError

class C(A):
    def foo(self): print(42)

C()  # works
