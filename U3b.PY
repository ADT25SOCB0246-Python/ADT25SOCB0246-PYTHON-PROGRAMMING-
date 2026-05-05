Program - Write a program to use the loop concept ‘for’ and ‘while’ loop.


# Taking input from user
num = int(input("Enter a number: "))

factorial = 1

# Using for loop
for i in range(1, num + 1):
    factorial = factorial * i

# Display result
print("Factorial of", num, "is:", factorial)

# Taking input from user
num = int(input("Enter a number: "))

factorial = 1
i = 1

# Using while loop
while i <= num:
    factorial = factorial * i
    i += 1

# Display result
print("Factorial of", num, "is:", factorial)