Program: Write a program to demonstrate the syntax and structure of user defined functions.

Title: Write a Python program to find the factorial of a user-defined number using a user-defined function.

# User Defined Function to calculate factorial

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Main Program
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial(num)
    print("Factorial of", num, "is", result)