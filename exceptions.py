try:
    # x = float(input("Num1"))
    # y = float(input("Num2"))
    x = 2
    y = 5
    result = x/y
except ValueError:
    print("Enter values pliss")
except ZeroDivisionError:
    print("Plis dont enter y as 0")
else:
    print(result)

import math
class sqrRoot(ArithmeticError):
    number = 0
    pass

    def squareRoot(self,number):
        self.number = number
        if self.number < 0:
            raise NegativeNumberError, \"Sqaure root of neg number not allowed"
        return math.sqrt(self.number)

a = sqrRoot()
print(a.squareRoot(-16))