Program - Write a program to print the first and last character of a string.


text = input("Enter a string: ")

first_char = text[0]
last_char_positive = text[len(text) - 1]

last_char_negative = text[-1]

print("First character (positive index):", first_char)
print("Last character (positive index):", last_char_positive)
print("Last character (negative index):", last_char_negative)