'''Find min and max using function'''

def smallest(lst): #function definition
   min_value = None
   for num in lst:
      if min_value is None or num < min_value:
         min_value = num
   return min_value


def largest(lst): #function definition
   max_value = None
   for num in lst:
      if max_value is None or num > max_value:
         max_value = num    
   return max_value

values = []
upto = int(input("Enter the number of values to add: "))
for i in range(upto):
   add = int(input(f"Enter number {i+1}: "))
   values.append(add)

# count = 0
# while count < upto:
#    add = int(input(f"Enter number {count+1}: "))
#    values.append(add)
#    count += 1

min = smallest(values) #function call
max = largest(values) #function call
print(f"Min Value: {min}\nMax Value: {max}")