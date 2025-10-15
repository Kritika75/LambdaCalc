"""
ΛambdaCalc - Open-source math library
"""

from algebra import complex_numbers, polynomials, ring_theory
from calculus import integration, differentiation, limits
from linear_algebra import eigenstuff, matrix_ops, vector_spaces
from number_theory import gcd_lcm, mod_arithmetic, primes

def main():
    print("Welcome to ΛambdaCalc!")
    print("A modular, beginner-friendly math library")
    print("\nAvailable modules:")
    print("- Complex Numbers")
    print("- Polynomials")
    print("- Ring Theory")
    print("- Linear Algebra")
    print("- Calculus")
    print("- Number Theory")
    
    # Quick Demo
    print("\n--- Quick Demo ---")
    print("\n1. Calculus - Definite Integration:")
    result = integration.definite_integral("x**2", 0, 1)
    print(f"   ∫₀¹ x² dx = {result}")
    
    print("\n2. Number Theory - GCD:")
    result = gcd_lcm.compute_gcd(48, 18)
    print(f"   GCD(48, 18) = {result}")
    
    
if __name__ == "__main__":
    main()