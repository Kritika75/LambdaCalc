#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, scrolledtext
from LambdaCalc.calculus.differentiation import differentiate_expression
from LambdaCalc.calculus.integration import indefinite_integral
from LambdaCalc.algebra.polynomials import add_polynomials, multiply_polynomials
import numpy as np

class LambdaCalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LambdaCalc - Mathematical Computing")
        self.root.geometry("600x500")
        self.dark_mode = False
        
        # Theme toggle button
        theme_frame = ttk.Frame(root)
        theme_frame.pack(fill='x', padx=10, pady=5)
        self.theme_btn = ttk.Button(theme_frame, text="🌙 Dark Mode", command=self.toggle_theme)
        self.theme_btn.pack(side='right')
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Calculus tab
        self.calc_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.calc_frame, text="Calculus")
        self.setup_calculus_tab(self.calc_frame)
        
        # Algebra tab
        self.algebra_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.algebra_frame, text="Algebra")
        self.setup_algebra_tab(self.algebra_frame)
    
    def setup_calculus_tab(self, frame):
        # Input
        ttk.Label(frame, text="Expression:").pack(pady=5)
        self.calc_entry = tk.Entry(frame, width=50)
        self.calc_entry.pack(pady=5)
        self.calc_entry.insert(0, "x**2 + 3*x + 2")
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Differentiate", command=self.differentiate).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Integrate", command=self.integrate).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_calc).pack(side='left', padx=5)
        
        # Output
        ttk.Label(frame, text="Result:").pack(pady=(20,5))
        self.calc_output = scrolledtext.ScrolledText(frame, height=15, width=70)
        self.calc_output.pack(fill='both', expand=True, pady=5)
    
    def setup_algebra_tab(self, frame):
        # Polynomial operations
        ttk.Label(frame, text="Polynomial 1 (coefficients):").pack(pady=5)
        self.poly1_entry = tk.Entry(frame, width=50)
        self.poly1_entry.pack(pady=5)
        self.poly1_entry.insert(0, "1,2,3")
        
        ttk.Label(frame, text="Polynomial 2 (coefficients):").pack(pady=5)
        self.poly2_entry = tk.Entry(frame, width=50)
        self.poly2_entry.pack(pady=5)
        self.poly2_entry.insert(0, "2,1")
        
        # Buttons
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=10)
        ttk.Button(btn_frame, text="Add", command=self.add_poly).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Multiply", command=self.multiply_poly).pack(side='left', padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_algebra).pack(side='left', padx=5)
        
        # Output
        ttk.Label(frame, text="Result:").pack(pady=(20,5))
        self.algebra_output = scrolledtext.ScrolledText(frame, height=15, width=70)
        self.algebra_output.pack(fill='both', expand=True, pady=5)
    
    def differentiate(self):
        expr = self.calc_entry.get()
        result = differentiate_expression(expr)
        self.calc_output.insert(tk.END, f"d/dx({expr}) = {result}\n")
        self.calc_output.see(tk.END)
    
    def integrate(self):
        expr = self.calc_entry.get()
        try:
            result = indefinite_integral(expr)
            self.calc_output.insert(tk.END, f"∫({expr})dx = {result}\n")
        except:
            self.calc_output.insert(tk.END, f"Integration of {expr} failed\n")
        self.calc_output.see(tk.END)
    
    def add_poly(self):
        try:
            p1 = [float(x.strip()) for x in self.poly1_entry.get().split(',')]
            p2 = [float(x.strip()) for x in self.poly2_entry.get().split(',')]
            result = add_polynomials(p1, p2)
            self.algebra_output.insert(tk.END, f"{p1} + {p2} = {result}\n")
        except Exception as e:
            self.algebra_output.insert(tk.END, f"Error: {e}\n")
        self.algebra_output.see(tk.END)
    
    def multiply_poly(self):
        try:
            p1 = [float(x.strip()) for x in self.poly1_entry.get().split(',')]
            p2 = [float(x.strip()) for x in self.poly2_entry.get().split(',')]
            result = multiply_polynomials(p1, p2)
            self.algebra_output.insert(tk.END, f"{p1} * {p2} = {result}\n")
        except Exception as e:
            self.algebra_output.insert(tk.END, f"Error: {e}\n")
        self.algebra_output.see(tk.END)
    
    def clear_calc(self):
        self.calc_output.delete(1.0, tk.END)
    
    def clear_algebra(self):
        self.algebra_output.delete(1.0, tk.END)
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            # Dark theme
            self.root.configure(bg='#2b2b2b')
            self.theme_btn.configure(text="☀️ Light Mode")
            self.calc_output.configure(bg='#3c3c3c', fg='white', insertbackground='white')
            self.algebra_output.configure(bg='#3c3c3c', fg='white', insertbackground='white')
        else:
            # Light theme
            self.root.configure(bg='SystemButtonFace')
            self.theme_btn.configure(text="🌙 Dark Mode")
            self.calc_output.configure(bg='white', fg='black', insertbackground='black')
            self.algebra_output.configure(bg='white', fg='black', insertbackground='black')

if __name__ == "__main__":
    root = tk.Tk()
    app = LambdaCalcGUI(root)
    root.mainloop()