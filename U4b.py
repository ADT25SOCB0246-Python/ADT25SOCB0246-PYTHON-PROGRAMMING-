Program: Write a program to import the developed modules.

Question: Write a Python program to import the developed module factorial and find the factorial of a user-defined number.

	
Step 1: Create a module file

Create a file named factorial.py

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


Step 2: Main program to import module

Create another file, for example main.py

import factorial

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    result = factorial.factorial(num)
    print("Factorial of", num, "is", result)