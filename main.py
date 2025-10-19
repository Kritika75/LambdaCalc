from algebra import *
from calculus import *
from linear_algebra import *
from number_theory import *
#from calculus import  differentiate_expression, indefinite_integral,definite_integral

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Interactive Math Explorer!📊")

topic= st.sidebar.selectbox(
    "**Select Topic ⬇️**",
    ["Algebra","Calculus","Linear Algebra","Number Theory"])

#----------------------------------ALGEBRA------------------------

if topic == "Algebra":
    operation= st.selectbox("Select Operation",[
        "Complex Numbers","Polynomials","Ring Theory"
    ])
    if operation == "Complex Numbers":
        a_real = st.number_input("Real Part of first Complex Number")
        a_imag = st.number_input("Imaginary Part of first Complex Number")
        b_real = st.number_input("Real Part of Second Complex Number")
        b_imag=  st.number_input("Imaginary Part of second Complex Number")

        op= st.selectbox("Operations", ["Addition","Subtraction","Multiplication","Division","Conjugate","Modulus"])

        if st.button("Compute"):
            z1= Complex(a_real,a_imag)
            z2= Complex(b_real,b_imag)
            if op== "Addition": st.success(z1+z2)
            elif op=="Subtraction": st.success(z1-z2)
            elif op== "Multiplication":st.success(z1*z2)
            elif op == "Division": st.success(z1/z2)
            elif op == "Conjugate": st.success(f"Conjugate z1: {z1.conjugate()},z2:{z2.conjugate()}")
            elif op == "Modulus": st.success(f"Modulus z1: {z1.modulus()}, z2: {z2.modulus()}")
            

    elif operation ==  "Polynomials":
        c1= st.text_input("Enter first Enter first polynomial coefficients (comma-separated)", "1,0,-2")
        c2= st.text_input("Enter second polynomial coefficients (comma-separated)", "1,-1")
        op = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide", "Derivative", "Integral", "Plot"])

        if st.button("Compute"):
            p1= Polynomial([float(c) for c in c1.split(",")])
            p2= Polynomial([float(c) for c in c2.split(",")])

            if op == "Add":st.success(p1.add(p2))
            elif op== "Subtract" : st.success(p1.subtract(p2))
            elif op == "Multiply": st.success(p1.multiply(p2))
            elif op == "Divide":
                q, r = p1.divide(p2)
                st.success(f"Quotient: {q}, Remainder: {r}")
            elif op == "Derivative": st.success(f"Derivative p1: {p1.derivative()}, p2: {p2.derivative()}")
            elif op == "Integral": st.success(f"Integral p1: {p1.integrate()}, p2: {p2.integrate()}")
            elif op== 'Plot':
                x= np.linspace(-10,10,400)
                y1= p1.evaluate(x)
                y2= p2.evaluate(x)
                fig,ax= plt.subplots()
                ax.plot(x,y1,label='p1')
                ax.plot(x,y2,label='p2')
                ax.legend()
                st.pyplot(fig)

    elif operation =='Ring Theory':
        mod= st.number_input("Enter Modulus for ℤ/nℤ",value=5)
        a= st.number_input("Enter a : ",value=2)
        b= st.number_input("Enter b: ",value=3)
        op = st.selectbox("Operation", ["Add", "Multiply","Subtract","Negate"])
        
        if st.button("Compute"):
            z= IntegerModRing(mod)
            a_ele= RingElement(a,z)
            b_ele= RingElement(b,z)
            if op== "Add":st.success(a_ele+b_ele)
            elif op== "Multiply": st.success(a_ele*b_ele)
            elif op== "Negate": st.success(-a_ele)
            elif op== "Subtract": st.success(a_ele-b_ele)
            

#---------------------------CALCULUS-------------------------------------

elif topic == "Calculus":
    operation = st.selectbox("Select Operations",[
        "Differentiation","Integration"])
    
    if operation== "Differentiation":
        expr = st.text_input("Enter the expression to differentiate","x**2 + 3*x")
        #var= st.text_input("Variable: ","x")
        if st.button("Compute Derivation"):
            result = differentiate_expression(expr)
            st.success(f"{result}")


    elif operation =="Integration":
        inte=  st.selectbox("Select Operation",["Indefinite Integral","Definite Integral"])
        if inte == "Indefinite Integral":
            exprs = st.text_input("Enter the expression for Indefinite Integral","x**2")
            if st.button("Compute Integral"):
                st.success(indefinite_integral(exprs))
        elif inte == "Definite Integral":
            exprs = st.text_input("Enter the expression for Definite Integral","x**2")
            a = st.number_input("Lower limit", value=0)
            b = st.number_input("Upper limit", value=1)
            if st.button("Compute Integral"):
                st.success(definite_integral(exprs, a,b))

#---------------------------------------LINEAR ALGEBRA-----------------------------

elif topic == "Linear Algebra":
    operation = st.selectbox("Select Operation",[
        "Matrix Operation","Vectors"
    ])

    if operation == "Matrix Operation":
        st.header("Matrix Operations")

    rows= st.number_input("Rows: ",min_value=1,max_value=5,value=2)
    cols= st.number_input("Cols : ",min_value=1,max_value=5,value=2)

    st.write("Enter Matrix A: ")
    A= np.array([st.text_input(f"A{i},{j}","1") 
                 for i in range(rows) for j in range(cols)],
                 dtype=float).reshape((rows,cols))
    
    st.write("Enter Matrix B")
    B=np.array([st.text_input(f"B{i},{j}","1")
                for i in range(rows) for j in range(cols)],
                dtype="float").reshape((rows,cols))
    
    operation = st.selectbox("Choose operation:", [
        "Add", "Multiply", "Transpose A", "Determinant A", "Inverse A", "Rank A", "Eigenvalues & Vectors"
    ])

    if st.button("Compute"):
        try:
            if operation == "Add":
                st.write(add_matrices(A, B))
            elif operation == "Multiply":
                st.write(multiply_matrices(A, B))
            elif operation == "Transpose A":
                st.write(transpose_matrix(A))
            elif operation == "Determinant A":
                st.write(determinant(A))
            elif operation == "Inverse A":
                st.write(inverse(A))
            elif operation == "Rank A":
                st.write(rank(A))
            elif operation == "Eigenvalues & Vectors":
                vals, vecs = eigenvalues_and_vectors(A)
                st.write("Eigenvalues:", vals)
                st.write("Eigenvectors:", vecs)
        except Exception as e:
            st.error(f"Error: {e}")
    

    elif operation == "Vectors":
        v1= st.text_input("Enter vector 1 (Coma seperated):","1,2")
        v2 = st.text_input("Enter vector 2 (coma seperated)","-2,1")

        v1= np.array(map(float,v1.split(",")))
        v2= np.array(map(float,v2.split(",")))

        operation = st.selectbox("Select Operation",[
            "Dot Product", "Check Orthogonality", "Norm of v1", "Projection of v1 onto v2"
        ])

        if st.button("Compute"):
            try:
                if operation == "Dot Product":
                    st.write(dot_product(v1, v2))
                elif operation == "Check Orthogonality":
                    st.write(is_orthogonal(v1, v2))
                elif operation == "Norm of v1":
                    st.write(norm(v1))
                elif operation == "Projection of v1 onto v2":
                    st.write(projection(v1, v2))
            except Exception as e:
                st.error(f"Error: {e}")

#------------------------------NUMBER THEORY--------------

elif topic == "Number Theory":
    operation = st.radio("**Select Operation:**",[
        "Check Prime", "Generate Primes", "Prime Factors"
    ])

    if operation == "Check Prime":
        s= st.number_input("Enter a Number: ",min_value=2, value=17)
        if st.button("Check"):
            st.write(f"{s} is prime? {check_prime(s)}")

    elif operation == "Generate Primes":
        start = st.number_input("Start: ",min_value=2, value=10)
        end= st.number_input("End: ",min_value=2, value=50)
        if st.button("Generate"):
            st.write(generate_primes(start,end))

    elif operation == "Prime Factors":
        n = st.number_input("Enter a number:", min_value=2, value=360)
        if st.button("Factorize"):
            st.write(get_prime_factors(n))