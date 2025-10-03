import numpy as np

class Polynomial:
    def __init__(self, coefficients):
        """
        coefficients: list or numpy array of coefficients,
        e.g., [1, 0, -2] represents 1*x^2 - 2
        """
        self.coefficients = np.trim_zeros(np.array(coefficients, dtype=float), 'f')

    def __str__(self):
        terms = []
        degree = len(self.coefficients) - 1
        for i, coef in enumerate(self.coefficients):
            power = degree - i
            if coef == 0:
                continue
            elif power == 0:
                terms.append(f"{coef:.2f}")
            elif power == 1:
                terms.append(f"{coef:.2f}x")
            else:
                terms.append(f"{coef:.2f}x^{power}")
        return " + ".join(terms).replace('+ -', '- ')

    def evaluate(self, x):
        return np.polyval(self.coefficients, x)

    def derivative(self):
        deriv_coeffs = np.polyder(self.coefficients)
        return Polynomial(deriv_coeffs)

    def integrate(self, constant=0):
        integ_coeffs = np.polyint(self.coefficients)
        integ_coeffs[-1] = constant
        return Polynomial(integ_coeffs)

    def add(self, other):
        return Polynomial(np.polyadd(self.coefficients, other.coefficients))

    def subtract(self, other):
        return Polynomial(np.polysub(self.coefficients, other.coefficients))

    def multiply(self, other):
        return Polynomial(np.polymul(self.coefficients, other.coefficients))

    def divide(self, other):
        quotient, remainder = np.polydiv(self.coefficients, other.coefficients)
        return Polynomial(quotient), Polynomial(remainder)


def add_polynomials(p1, p2):
    """Add two polynomials represented as coefficient lists."""
    return list(np.polyadd(p1, p2))

def multiply_polynomials(p1, p2):
    """Multiply two polynomials represented as coefficient lists."""
    return list(np.polymul(p1, p2))

def integrate_expression(expr_str):
    """Simple wrapper for integration."""
    from .integration import indefinite_integral
    return indefinite_integral(expr_str)

# Example usage
if __name__ == "__main__":
    p1 = Polynomial([1, 0, -2])  # x^2 - 2
    p2 = Polynomial([1, -1])     # x - 1

    print("P1:", p1)
    print("P2:", p2)
    print("P1 + P2:", p1.add(p2))
    print("P1 - P2:", p1.subtract(p2))
    print("P1 * P2:", p1.multiply(p2))
    q, r = p1.divide(p2)
    print("P1 / P2:", q, "Remainder:", r)
    print("P1 evaluated at x=2:", p1.evaluate(2))
    print("P1 derivative:", p1.derivative())
    print("P1 integral:", p1.integrate())
