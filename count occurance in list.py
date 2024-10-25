"""write a function that counts the occurence of each element in the list=[1, 2, 3, 1, 2, 1, 4, 1]"""

list_values = [1, 2, 3, 1, 2, 1, 4, 1]
sorted_list = []

for i in list_values:
   if i not in sorted_list:
      sorted_list.append(i)      #checking and filtering unique values

for i in sorted_list:
   count = list_values.count(i)
   print(f"The value {i} occurred {count} times.")      #finding the count of each value
