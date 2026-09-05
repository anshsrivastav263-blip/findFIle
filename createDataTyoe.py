from math import gcd


class Fraction:

    def __init__(self, n, d):
        if d == 0:
            raise ValueError("Denominator cannot be zero")

        # Make denominator positive
        if d < 0:
            n = -n
            d = -d

        # Simplify fraction
        common = gcd(n, d)

        self.n = n // common
        self.d = d // common

    def __str__(self):
        return f"{self.n}/{self.d}"

    def __add__(self, other):
        temp_n = self.n * other.d + self.d * other.n
        temp_d = self.d * other.d

        # return the object value   Fraction(n value,d value) 
        return Fraction(temp_n, temp_d)

    def __sub__(self, other):
        temp_n = self.n * other.d - self.d * other.n
        temp_d = self.d * other.d

        # return the object value   Fraction(n value,d value) 
        return Fraction(temp_n, temp_d)

    def __mul__(self, other):
        temp_n = self.n * other.n
        temp_d = self.d * other.d

        # return the object value   Fraction(n value,d value) 
        return Fraction(temp_n, temp_d)

    def __truediv__(self, other):
        if other.n == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        temp_n = self.n * other.d
        temp_d = self.d * other.n

        # return the object value   Fraction(n value,d value) 
        return Fraction(temp_n, temp_d)


# First fraction
num1 = int(input("Enter numerator: "))
den1 = int(input("Enter denominator: "))

f1 = Fraction(num1, den1)


# Second fraction
num2 = int(input("Enter numerator: "))
den2 = int(input("Enter denominator: "))

f2 = Fraction(num2, den2)


# Display fractions
print("\nFraction 1:", f1)
print("Fraction 2:", f2)


# Operations
print("\nAddition:", f1 + f2)
print("Subtraction:", f1 - f2)
print("Multiplication:", f1 * f2)
print("Division:", f1 / f2)