Program - Write a program to understand the concept of indexing.

# Taking input from user
text = input("Enter a string: ")

# Positive indexing
print("\nUsing Positive Indexing:")
print("First character (index 0):", text[0])
print("Second character (index 1):", text[1])
print("Last character (index len-1):", text[len(text)-1])

# Negative indexing
print("\nUsing Negative Indexing:")
print("Last character (index -1):", text[-1])
print("Second last character (index -2):", text[-2])
print("First character (index -len):", text[-len(text)])