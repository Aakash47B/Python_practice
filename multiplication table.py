'''Homework: Write a program to print a multiplication table. If user gives 5 as input, print multiplication table of 5.'''

multiple = int(input("Enter a number to generate multiplication table: "))
upto = int(input("Enter the range of the multiplication: "))

print(f"multiplication table of {multiple}")
for mul in range(1,upto+1):
   print(f"{multiple} x {mul} = {mul * multiple}")