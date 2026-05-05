Program: Write a program that opens a file and then reads the contents of the file. The program should then print out the contents of the file.

try:
    file_name = input("Enter the file name: ")
    
    with open(file_name, 'r') as file:
        content = file.read()
        print("\nFile Contents:\n")
        print(content)

except FileNotFoundError:
    print("Error: File not found.")

except IOError:
    print("Error: Unable to read the file.")

finally:
    print("\nProgram execution completed.")