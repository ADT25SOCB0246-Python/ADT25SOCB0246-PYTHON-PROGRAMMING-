Program - Write a program that prompts the user to enter their age and prints out their age in years, months, and days.


 
age_years = int(input("Enter your age in years: "))

 
months = age_years * 12
days = age_years * 365    

 
print("Your age is:")
print("Years:", age_years)
print("Months:", months)
print("Days:", days)