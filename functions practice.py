'''Write a function remove_spaces(s) that removes all spaces from a given string s using a while loop.'''

# def remove_spaces(s):
#    s_without_spaces = ""
#    index_val = 0
#    while index_val < len(s):
#       if s[index_val] != ' ':
#          s_without_spaces += s[index_val]
#       index_val += 1
#    return s_without_spaces
# s = input("Enter a sentence: ").lower()

# print(remove_spaces(s))

'''Write a function sum_numbers(n) that calculates the sum of all numbers from 1 to n using a while loop. '''

# import sys
# def sum_numbers(n):
#    sum = 0
#    while n != 0:
#       sum += n
#       n -= 1
#    return sum

# num = int(input("Enter num: "))

# if num < 0: #if i/p is negative, converts to positive value
#    num = num * -1
# if num == 0: # if i/p is 0 then exit
#    print(0)
#    sys.exit(0)
# print(sum_numbers(num))

'''Write a function factorial(n) that calculates the factorial of a given number n using a while loop.'''

# import sys

# def factorial(n):
#    sum = 1
#    while n != 1:
#       sum *= n
#       n -= 1
#    return sum
   
# num = int(input("Enter num: "))

# if num < 0: #if i/p is negative, converts to positive value
#    num = num * -1
# if num == 0: # if i/p is 0 then factorial of 0 is 1
#    print(1)
#    sys.exit(0)

# print(factorial(num))

'''Write a function replace_char(s, old, new) that replaces all occurrences of the character old with the character new in a string s using a while loop.'''

# def replace_char(s, old, new): 
#    replaced_word =""
#    index_val = 0

#    while index_val < len(s):
#       if s[index_val] == old:
#          # s[index_val] == new
#          replaced_word += new
#          index_val += 1
#       else:
#          replaced_word += s[index_val]
#          index_val += 1

#    return replaced_word
# s = input("Enter a sentence: ").lower()
# find = input("Enter the word to find: ")
# replace = input("Enter the word to replace: ")
# print(replace_char(s,find,replace))

'''Write a function find_largest(lst) that finds and returns the largest number in a list using a while loop.'''

# def add_value(range):
#    num_list = []
#    count = 0
#    while count < range:
#       val = int(input(f"Enter num {count+1} :"))
#       num_list.append(val)
#       count +=1
#    return num_list

# def find_largest(lst):
#    largest_val,index_val = 0,0
#    while index_val < len(lst):
#       if lst[index_val] > largest_val:
#          largest_val = lst[index_val]
#       index_val += 1
#    return largest_val

# range = int(input("The how many values to add: "))
# lst = add_value(range)

# print(f"The largest num is {find_largest(lst)}")