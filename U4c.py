Program: Write a program to use the class and object concept.

Question: Write a Python program to use the class and object concept to find the factorial of a user-defined number.

class Factorial:
    def __init__(self, num):
        self.num = num

    def find_factorial(self):
        fact = 1
        for i in range(1, self.num + 1):
            fact = fact * i
        print("Factorial of", self.num, "is", fact)

# Main Program
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial does not exist for negative numbers.")
else:
    obj = Factorial(n)   # Object creation
    obj.find_factorial() # Method call
