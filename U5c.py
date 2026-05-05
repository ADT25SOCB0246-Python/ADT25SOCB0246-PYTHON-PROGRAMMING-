Program: Write a program that uses SymPy to calculate the derivative of the function f(x) = x^2.

from sympy import symbols, diff

# Define the variable
x = symbols('x')

# Define the function
f = x**2

# Calculate the derivative
derivative = diff(f, x)

# Print the result
print("Function f(x) =", f)
print("Derivative f'(x) =", derivative)