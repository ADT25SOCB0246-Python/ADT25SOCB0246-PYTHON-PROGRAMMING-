Program: Write a program to understand the concept of Polymorphism, overloading and overriding.

Type(1): Compile Time Polymorphism or Method Overloading Polymorphism.

Question: Write a Python program to demonstrate Compile Time / Method Overloading polymorphism using simple class-object concept by performing addition of different data types such as integers, floating-point numbers, and complex numbers using the same method.

class Addition:
    def display(self, x, y):
        print("Addition is:", x + y)
 
obj = Addition()

print("Addition of integers:")
obj.display(10, 20)

print("\nAddition of floats:")
obj.display(1.1, 2.2)

print("\nAddition of complex numbers:")
obj.display(2 + 3j, 4 + 5j)