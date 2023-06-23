class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return ComplexNumber(real_part, imag_part)

# Define the complex numbers as objects of the ComplexNumber class
num1 = ComplexNumber(3, 4)
num2 = ComplexNumber(1, 2)

# Perform the addition using the + operator
result = num1 + num2

# Print the result
print(f"The sum of {num1.real}+{num1.imag}j and {num2.real}+{num2.imag}j is {result.real}+{result.imag}j")