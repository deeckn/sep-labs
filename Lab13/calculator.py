class Calculator:
    def __init__(self):
        self.acc: float = 0.0

    def set_accumulator(self, a):
        self.verify_number(a)
        self.acc = a

    def get_accumulator(self):
        return self.acc

    def add(self, x):
        self.verify_number(x)
        self.acc += x

    def subtract(self, x):
        self.verify_number(x)
        self.acc -= x

    def multiply(self, x):
        self.verify_number(x)
        self.acc *= x

    def divide(self, x):
        self.verify_number(x)
        self.verify_zero(x)
        self.acc /= x

    def get_status(self):
        return f"Result: {self.acc}"

    def verify_zero(self, x):
        if x == 0:
            raise ZeroDivisionError("Zero division error")

    def verify_number(self, x):
        if not isinstance(x, int) or isinstance(x, float):
            raise TypeError("Not a number")
