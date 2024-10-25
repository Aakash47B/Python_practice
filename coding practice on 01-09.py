# word=input("Enter a string").lower()
# start_index=0
# count=0
# vowel_list=['a','e','i','o','u']

# while start_index <len(word):
#    if word[start_index] in vowel_list:
#       count+=1
#    start_index+=1

# print(count)

"""enter value from till user says end"""

# bag=[]
# purchase = ""
# while purchase != "end":

#    item = input("Enter item: ")
#    bag.append(item)
#    purchase = input("end?")

# print(bag)
"""Home Work"""

'''Write a function remove_spaces(s) that removes all spaces from a given string s using a while loop.'''

# s = input("Enter a sentence: ").lower()

# s_without_spaces = ""
# index_val = 0
# while index_val < len(s):
#    if s[index_val] != ' ':
#       s_without_spaces += s[index_val]
#    index_val += 1

# print(s_without_spaces)


'''Write a function sum_numbers(n) that calculates the sum of all numbers from 1 to n using a while loop. '''

# import sys
# num = int(input("Enter num: "))
# sum = 0

# if num < 0: #if i/p is negative, converts to positive value
#    num = num * -1
# if num == 0: # if i/p is 0 then exit
#    print(0)
#    sys.exit(0)

# while num != 0:
#    sum += num
#    num -= 1

# print(sum)

'''Write a function factorial(n) that calculates the factorial of a given number n using a while loop.'''

# import sys
# num = int(input("Enter num: "))

# if num < 0: #if i/p is negative, converts to positive value
#    num = num * -1
# if num == 0: # if i/p is 0 then factorial of 0 is 1
#    print(1)
#    sys.exit(0)

# factorial = 0
# sum = 1

# while num != 1:
#    sum *= num
#    num -= 1

# print(sum)

'''Write a function replace_char(s, old, new) that replaces all occurrences of the character old with the character new in a string s using a while loop.'''

# s = input("Enter a sentence: ").lower()

# s_without_occurrence = ""
# index_val = 0

# while index_val < len(s):
#    if s[index_val] not in s_without_occurrence:
#       s_without_occurrence += s[index_val]
#    index_val += 1

# print(s_without_occurrence)


'''Write a function find_largest(lst) that finds and returns the largest number in a list using a while loop.'''


# num_list = []
# range = int(input("The how many values to add: "))
# count = 0
# while count < range:
#    val = int(input(f"Enter num {count+1} :"))
#    num_list.append(val)
#    count +=1 


# num_list = [10,20,30,40,50]

# largest_val,index_val = 0,0

# while index_val < len(num_list):
#    if num_list[index_val] > largest_val:
#       largest_val = num_list[index_val]
#    index_val += 1

# print(largest_val)
