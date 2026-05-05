Program - Write a program to demonstrate the concept of data types & conversion.

num_int = 10
print("Integer value:", num_int, "Type:", type(num_int))

num_float = 10.5
print("Float value:", num_float, "Type:", type(num_float))

char = 'A'
print("Character value:", char, "Type:", type(char))

text = "Hello Python"
print("String value:", text, "Type:", type(text))

flag = True
print("Boolean value:", flag, "Type:", type(flag))

# Integer to Float
a = float(num_int)
print("\nInteger to Float:", a, "Type:", type(a))

# Float to Integer
b = int(num_float)
print("Float to Integer:", b, "Type:", type(b))

# Integer to String
c = str(num_int)
print("Integer to String:", c, "Type:", type(c))

# String to Integer
d = int("20")
print("String to Integer:", d, "Type:", type(d))

# Boolean to Integer
e = int(flag)
print("Boolean to Integer:", e, "Type:", type(e))