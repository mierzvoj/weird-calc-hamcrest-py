import math

import numpy as np


class Calculator:
    def __init__(self, a=0, b=0, c=0, d=0, str1="", str2=""):
        self.a: float = a
        self.b: float = b
        self.c: int = c
        self.d: int = d
        self.str1 = str1
        self.str2 = str2

    def summary(self) -> float:
        return self.a + self.b

    def multiply(self) -> int:
        return self.c * self.d

    def reverse(self) -> str:
        return self.str1[::-1]

    def concat(self) -> str:
        return self.str1 + self.str2


res = Calculator(3.0, 8.4, 3, 6, "ala ma kota", "ala ma kota")
print(res.summary())
print(res.multiply())
print(res.reverse())
print(res.concat())
# res1 = Calculator("a", 8.4, 3, 6, "ala ma kota")
# print(res1.summary())