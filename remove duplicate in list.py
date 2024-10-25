"""write a function that removes duplicates from original_list=[1, 2, 2, 3, 4, 4, 5]"""

original_list=[1, 2, 2, 3, 4, 4, 5]
new_list = []

for i in original_list:          
   if i not in new_list:          #checking and filtering unique values
      new_list.append(i)

print(new_list)  