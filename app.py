#!/usr/bin/env python3
"""
ΛambdaCalc Web Server
A Flask-based web server that provides API endpoints for the LambdaCalc math library.
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import json
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import LambdaCalc modules
from algebra.complex_numbers import Complex
from algebra.polynomials import Polynomial
from linear_algebra.matrix_ops import *
from calculus.differentiation import differentiate_expression
from calculus.integration import indefinite_integral, definite_integral
from calculus.limits import compute_limit
from number_theory.gcd_lcm import compute_gcd, compute_lcm
from number_theory.primes import check_prime, generate_primes
from utils.helpers import safe_eval
from utils.input_parser import parse_matrix, parse_polynomial

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

@app.route('/')
def index():
    """Serve the main calculator interface."""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Calculator interface not found. Please ensure index.html exists.", 404

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """Handle basic arithmetic calculations."""
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        if not expression:
            return jsonify({'error': 'No expression provided'}), 400
        
        # Use safe_eval for basic arithmetic
        result = safe_eval(expression)
        
        if result is None:
            return jsonify({'error': 'Invalid expression'}), 400
        
        return jsonify({
            'result': result,
            'expression': expression
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/matrix', methods=['POST'])
def matrix_operations():
    """Handle matrix operations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        matrix_a = data.get('matrixA')
        matrix_b = data.get('matrixB')
        
        if not operation:
            return jsonify({'error': 'No operation specified'}), 400
        
        # Parse matrices
        if matrix_a:
            matrix_a = parse_matrix(matrix_a)
        if matrix_b:
            matrix_b = parse_matrix(matrix_b)
        
        result = None
        
        if operation == 'add':
            if not matrix_a or not matrix_b:
                return jsonify({'error': 'Both matrices required for addition'}), 400
            result = add_matrices(matrix_a, matrix_b)
        
        elif operation == 'multiply':
            if not matrix_a or not matrix_b:
                return jsonify({'error': 'Both matrices required for multiplication'}), 400
            result = multiply_matrices(matrix_a, matrix_b)
        
        elif operation == 'inverse':
            if not matrix_a:
                return jsonify({'error': 'Matrix A required for inverse'}), 400
            result = inverse(matrix_a)
        
        elif operation == 'determinant':
            if not matrix_a:
                return jsonify({'error': 'Matrix A required for determinant'}), 400
            result = determinant(matrix_a)
        
        elif operation == 'transpose':
            if not matrix_a:
                return jsonify({'error': 'Matrix A required for transpose'}), 400
            result = transpose_matrix(matrix_a)
        
        else:
            return jsonify({'error': 'Unknown matrix operation'}), 400
        
        return jsonify({
            'result': result,
            'operation': operation
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/calculus', methods=['POST'])
def calculus_operations():
    """Handle calculus operations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        function = data.get('function')
        variable = data.get('variable', 'x')
        
        if not operation or not function:
            return jsonify({'error': 'Operation and function required'}), 400
        
        result = None
        
        if operation == 'differentiate':
            result = str(differentiate_expression(function, variable))
        
        elif operation == 'integrate':
            result = str(indefinite_integral(function, variable))
        
        elif operation == 'limit':
            point = data.get('point', 0)
            direction = data.get('direction', '+')
            result = str(compute_limit(function, variable, point, direction))
        
        else:
            return jsonify({'error': 'Unknown calculus operation'}), 400
        
        return jsonify({
            'result': result,
            'operation': operation,
            'function': function
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/complex', methods=['POST'])
def complex_operations():
    """Handle complex number operations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        real_a = data.get('realA', 0)
        imag_a = data.get('imagA', 0)
        real_b = data.get('realB', 0)
        imag_b = data.get('imagB', 0)
        
        if not operation:
            return jsonify({'error': 'No operation specified'}), 400
        
        complex_a = Complex(real_a, imag_a)
        complex_b = Complex(real_b, imag_b)
        
        result = None
        
        if operation == 'add':
            result = complex_a + complex_b
        elif operation == 'subtract':
            result = complex_a - complex_b
        elif operation == 'multiply':
            result = complex_a * complex_b
        elif operation == 'divide':
            result = complex_a / complex_b
        elif operation == 'magnitude':
            result = complex_a.magnitude()
        elif operation == 'phase':
            result = complex_a.phase()
        else:
            return jsonify({'error': 'Unknown complex operation'}), 400
        
        return jsonify({
            'result': {
                'real': result.real if hasattr(result, 'real') else result,
                'imag': result.imag if hasattr(result, 'imag') else 0,
                'magnitude': result.magnitude() if hasattr(result, 'magnitude') else abs(result),
                'phase': result.phase() if hasattr(result, 'phase') else 0
            },
            'operation': operation
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/polynomial', methods=['POST'])
def polynomial_operations():
    """Handle polynomial operations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        coeffs_a = data.get('coefficientsA', [])
        coeffs_b = data.get('coefficientsB', [])
        
        if not operation or not coeffs_a:
            return jsonify({'error': 'Operation and coefficients A required'}), 400
        
        poly_a = Polynomial(coeffs_a)
        poly_b = Polynomial(coeffs_b) if coeffs_b else None
        
        result = None
        
        if operation == 'evaluate':
            x = data.get('x', 0)
            result = poly_a.evaluate(x)
        
        elif operation == 'derivative':
            result = poly_a.derivative()
        
        elif operation == 'integrate':
            constant = data.get('constant', 0)
            result = poly_a.integrate(constant)
        
        elif operation == 'add' and poly_b:
            result = poly_a.add(poly_b)
        
        elif operation == 'subtract' and poly_b:
            result = poly_a.subtract(poly_b)
        
        elif operation == 'multiply' and poly_b:
            result = poly_a.multiply(poly_b)
        
        else:
            return jsonify({'error': 'Unknown polynomial operation'}), 400
        
        return jsonify({
            'result': str(result),
            'operation': operation
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/number-theory', methods=['POST'])
def number_theory_operations():
    """Handle number theory operations."""
    try:
        data = request.get_json()
        operation = data.get('operation')
        a = data.get('a')
        b = data.get('b')
        
        if not operation:
            return jsonify({'error': 'No operation specified'}), 400
        
        result = None
        
        if operation == 'gcd':
            if a is None or b is None:
                return jsonify({'error': 'Two numbers required for GCD'}), 400
            result = compute_gcd(a, b)
        
        elif operation == 'lcm':
            if a is None or b is None:
                return jsonify({'error': 'Two numbers required for LCM'}), 400
            result = compute_lcm(a, b)
        
        elif operation == 'is_prime':
            if a is None:
                return jsonify({'error': 'Number required for prime check'}), 400
            result = check_prime(a)
        
        elif operation == 'generate_primes':
            if a is None:
                return jsonify({'error': 'Limit required for prime generation'}), 400
            result = generate_primes(2, a)
        
        else:
            return jsonify({'error': 'Unknown number theory operation'}), 400
        
        return jsonify({
            'result': result,
            'operation': operation
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'service': 'LambdaCalc API',
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("🧠📐 ΛambdaCalc Web Server Starting...")
    print("=" * 50)
    print("Available endpoints:")
    print("  GET  /              - Calculator interface")
    print("  POST /api/calculate - Basic arithmetic")
    print("  POST /api/matrix    - Matrix operations")
    print("  POST /api/calculus  - Calculus operations")
    print("  POST /api/complex   - Complex number operations")
    print("  POST /api/polynomial - Polynomial operations")
    print("  POST /api/number-theory - Number theory operations")
    print("  GET  /api/health    - Health check")
    print("=" * 50)
    print("Starting server on http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
