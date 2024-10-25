"""1. Calcualte and print users age - Write a program to ask the user for his/her name and print 'Hello', user's name. 
Ask what year they were born.  get the year from the user. Print 'You are <age> years old'."""

name = input("Enter your name: ")
print("Hello ",name)

year_born = int(input("Which year were you born: "))
current_year = 2024
age = current_year - year_born
print(f"You are {age} years old.")