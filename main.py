#!/usr/bin/env python3
"""
LambdaCalc - A Mathematical Computing Library
Main entry point for the application
"""

import sys
from LambdaCalc.utils.display import print_title
from LambdaCalc.calculus.differentiation import differentiate_expression

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--gui":
        # Launch GUI
        import tkinter as tk
        from gui import LambdaCalcGUI
        root = tk.Tk()
        app = LambdaCalcGUI(root)
        root.mainloop()
    else:
        # Console mode
        print_title("LambdaCalc - Mathematical Computing Library")
        print("Welcome to LambdaCalc!")
        print("This library provides mathematical computing capabilities including:")
        print("- Calculus (differentiation, integration, limits)")
        print("- Linear Algebra (matrices, vectors, eigenvalues)")
        print("- Algebra (polynomials, complex numbers, ring theory)")
        print("- Number Theory (GCD/LCM, modular arithmetic, primes)")
        print("\nRun 'python main.py --gui' to launch the GUI interface")
        
        # Example usage
        print_title("Example: Differentiation")
        expr = "x**2 + 3*x + 2"
        result = differentiate_expression(expr)
        print(f"d/dx of {expr} = {result}")

if __name__ == "__main__":
    main()