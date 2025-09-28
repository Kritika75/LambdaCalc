# complex.py

import math

class Complex:
    """
    A class to represent complex numbers and perform basic arithmetic.

    Attributes:
        real (float): The real part of the complex number.
        imag (float): The imaginary part of the complex number.
    """
    def __init__(self, real=0, imag=0):
        """Initializes a Complex number instance."""
        self.real = real
        self.imag = imag

    def __repr__(self):
        """Provides a developer-friendly string representation."""
        if self.imag >= 0:
            return f"({self.real} + {self.imag}i)"
        return f"({self.real} - {-self.imag}i)"

    def __add__(self, other):
        """Adds two complex numbers."""
        if not isinstance(other, Complex):
            # Allow adding real numbers (e.g., c1 + 5)
            other = Complex(other)
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        """Subtracts one complex number from another."""
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        """Multiplies two complex numbers."""
        if not isinstance(other, Complex):
            other = Complex(other)
        
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        """Divides one complex number by another."""
        if not isinstance(other, Complex):
            other = Complex(other)
            
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number (0+0i).")
            
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    def magnitude(self):
        """Calculates the magnitude (or modulus) of the complex number."""
        return math.sqrt(self.real**2 + self.imag**2)

    def conjugate(self):
        """Returns the complex conjugate."""
        return Complex(self.real, -self.imag)

# This block demonstrates how the class works.
# It only runs when you execute this script directly (e.g., "python complex.py").
# It will not run if you import the `Complex` class into another file.
if __name__ == "__main__":
    print("--- Complex Number Demonstration ---")

    # Create instances of complex numbers
    c1 = Complex(3, 4)
    c2 = Complex(1, -2)

    print(f"\nc1 = {c1}")
    print(f"c2 = {c2}")

    # --- Perform operations ---
    print("\n--- Arithmetic Operations ---")
    sum_result = c1 + c2
    diff_result = c1 - c2
    prod_result = c1 * c2
    div_result = c1 / c2
    
    print(f"c1 + c2 = {sum_result}")
    print(f"c1 - c2 = {diff_result}")
    print(f"c1 * c2 = {prod_result}")
    print(f"c1 / c2 = {div_result}")

    # --- Other methods ---
    print("\n--- Other Methods ---")
    print(f"Magnitude of c1 = {c1.magnitude():.2f}")
    print(f"Conjugate of c1 = {c1.conjugate()}")
    
    # --- Operations with real numbers ---
    print("\n--- Operations with Real Numbers ---")
    c3 = c1 + 5  # Example of adding a real number
    c4 = c1 * 2  # Example of multiplying by a real number
    
    print(f"c1 + 5 = {c3}")
    print(f"c1 * 2 = {c4}")

    print("\n--- Demonstration Complete ---")