Program: Write a program to understand the concept of Polymorphism, overloading and overriding.

Type(2): Run Time Polymorphism or Method Overriding Polymorphism.

Write a Python program to demonstrate runtime/Method Overriding polymorphism by performing addition of integers, floating-point numbers, and complex numbers through different classes.

class Addition:
    def display(self, x, y):
        print("Addition is:", x + y)

class FloatAddition(Addition):
    def display(self, x, y):
        print("Addition of floats is:", x + y)

class ComplexAddition(Addition):
    def display(self, x, y):
        print("Addition of complex numbers is:", x + y)

obj1 = Addition()
print("Addition of integers:")
obj1.display(10, 20)

obj2 = FloatAddition()
print("\nAddition of floats:")
obj2.display(1.1, 2.2)

obj3 = ComplexAddition()
print("\nAddition of complex numbers:")
obj3.display(2 + 3j, 4 + 5j)


 

