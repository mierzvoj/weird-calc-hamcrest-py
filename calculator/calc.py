import math

import numpy as np


class Calculator:
    def __init__(self):
        self.basic()
        self.scientific()
        self.a: float = None
        self.b: float = None
        self.op: str = None
        self.summary(self, self.a, self.b)

    def summary(self, a, b):
        return a + b

    def substr(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def basic(self):
        # =============================================================================
        #     +     for a + b
        #     -     for a - b
        #     /     for a / b
        #     *     for a * b
        # =============================================================================
        op = input(
            'What kind of operation would you like to do?\
            \nChoose between "+, -, *, /" : ')

        a = float(input('Please type the first number: '))
        b = float(input('Please type the second number: '))

        if op == '+':
            print(self.summary(self.a, self.b))
        elif op == '-':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b)
        elif op == '*':
            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b)
        elif op == '/':
            if b == 0:
                return 'Error: Cannot be divided by 0'
            else:
                return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b)
        else:
            return "Incorrect operator! Please select from the given options!"

    def scientific(self):
        # =============================================================================
        #     ^     for a ^ b
        #     %     for a mod b
        #     r     for the bth root of a (a ^ (1/b))
        #     !     for a factorial
        #     sin   for sin(a) in deg
        #     cos   for cos(a) in deg
        #     tan   for tan(a) in deg
        #     ln    for ln(a) (log base e of a)
        # =============================================================================

        op = input(
            'Choose between "^, r, %, !, sin, cos, tan, ln" : ')
        if op == '^' or op == '%' or op == 'r':

            a = int(input('Please type the first number: '))
            b = int(input('Please type the second number: '))
        else:
            a = int(input('Please type the input number: '))

        if op == '^':

            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** b)

        elif op == '%':

            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a % b)

        elif op == 'r':

            return str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a ** (1 / b))

        elif op == '!':

            return ' = ' + str(math.factorial(a))

        elif op == 'sin':

            return ' = ' + str(math.radians(a))

        elif op == 'cos':

            return ' = ' + str(math.radians(a))

        elif op == 'tan':

            return ' = ' + str(math.radians(a))

        elif op == 'ln':

            return ' = ' + str(np.log(a))

        else:
            return "Incorrect operator! Please select from the given options!"

    def main(self):
        print("""Choose a calculator
        1. Basic Calculator
        2. Scientific Calculator""")
        choice = int(input('Please choose as 1 or 2: '))

        if choice == 1:
            print(self.basic())

        elif choice == 2:
            print(self.scientific())

        else:
            print('Invalid choice! Please select between 1 and 2:')


calc1 = Calculator()
calc1.main()
