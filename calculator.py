class QuickCalc:
    def __init__(self):
        self.current_value = 0.0

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def clear(self):
        self.current_value = 0.0
        return self.current_value