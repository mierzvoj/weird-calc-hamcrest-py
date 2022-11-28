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

    def get_range(self):
        try:
            if self.a >= 0 and self.a < 3:
                return 'B'
            if self.b >= 1 and self.b <= 3:
                return 'A'
            if self.b < 0 or self.b > 100:
                raise ValueError('Invalid value')
        except Exception as e:
            print('Value error!')
            raise

    def negativeFunctionVal(self):
        try:
            if self.multiply() < 0:
                raise ValueError('Invalid value')
        except Exception as e:
            print('Value error!')
            raise


res = Calculator(3.0, 8.4, 3, 6, "ala ma kota", "ala ma kota")
print(res.summary())
print(res.multiply())
print(res.reverse())
print(res.concat())

