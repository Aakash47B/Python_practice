"""Ask the user to input 3 numbers. Ask the user if they want to find the max of these numbers or mininum.
Find the answer and print."""

values = []
min_value = 0
max_value = 0

for i in range(3):
   num = int(input(f"Enter number {i+1}: "))
   values.append(num)

choice = int(input("Find Min(1) or Max(2): "))

# if choice == 1:
#    print(min(values))

# if choice == 2:
#    print(max(values))

if choice == 1:
   for num in values:
      if num < min_value or min_value == 0:
         min_value = num
   print(min_value)      

if choice == 2:
   for num in values:
      if num > max_value:
         max_value = num
   print(max_value)      