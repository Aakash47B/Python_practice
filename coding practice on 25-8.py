"""Write a function count_vowels(s) that takes a string s and returns the number of vowels (a, e, i, o, u) in the string. The function should be case-insensitive."""

# vowels = ["a","e","i","o","u"]

# word = input("Enter the word: ").lower()
# count = 0

# for vowel in vowels:
#    counter = word.count(vowel)
#    if vowel in word:
#       count += counter
#    print(f"the vowel {vowel} occured {counter} times")
# print(f"The no of times vowels occured is {count}")

'''Description: Write a function find_max_min(lst) that takes a list of integers lst and returns a tuple with the maximum and minimum values in the list.
find_max_min([3, 5, 1, 9, 7])  # Output: (9, 1)
find_max_min([-10, 0, 5, 12, 3])  # Output: (12, -10)'''

# min_value = None
# max_value = 0
# lst = []
# for value in range(5):
#    ip = int(input("enter val: "))
#    lst.append(ip)
# print(lst)

# for current_value1 in lst:
#    if min_value == None:
#       min_value = current_value1

#    elif min_value > current_value1:
#       min_value = current_value1


# for current_value2 in lst:
#    if max_value < current_value2:
#       max_value = current_value2

# print(max_value,min_value)



'''remove duplicates [1,2,2,3,4,4,5]
remove duplicates [apple,banana,apple,orange]
step1 create a list containing values
step2 create a new empty list "new_lst" to store values which are not duplicate
step3 write a for loop as for val in lst to fetch one value at a time
step4 write a if condition if val not in new_list
step5 adding values which are not duplicate
step6 print list
'''

# lst = [1,2,2,3,4,4,5]
# # lst = ["apple","banana","apple","orange"]
# new_lst = []
# for val in lst:
#    if val not in new_lst:
#       new_lst.append(val)
# print(new_lst)

"""List and Loop - Splitting and Summing Even and Odd Numbers*
Description: Write a function sum_even_odd(lst) that takes a list of integers lst and returns a tuple with the sum of even numbers and the sum of odd numbers in the list.

sum_even_odd([1, 2, 3, 4, 5, 6])  # Output: (12, 9)
sum_even_odd([10, 21, 32, 43, 54])  # Output: (96, 64)

*Steps:*
1. Initialize two variables to store the sum of even and odd numbers.
2. Loop through the list and check if each number is even or odd.
3. Add even numbers to the even sum and odd numbers to the odd sum.
4. Return the sums as a tuple."""

# # lst = [1,2,3,4,5,6]
# lst = [10,21,32,43,54]
# odd_val = 0
# even_val = 0

# for val in lst:
#    if val % 2==0:
#       even_val += val
#    else:
#       odd_val += val

# print(f"odd values are {odd_val} and even values are {even_val}")

'''*String and Loop - Checking for a Palindrome*
Description: Write a function is_palindrome(s) that takes a string s and returns True if the string is a palindrome (reads the same forward and backward), ignoring spaces and case, and False otherwise.is_palindrome("racecar")  # Output: True
is_palindrome("A man a plan a canal Panama")  # Output: True
is_palindrome("hello")  # Output: False*Steps*:
Normalize the string by converting it to lowercase and removing spaces.
Use a loop to compare characters from the beginning and end of the string moving toward the center.
Return True if all characters match, otherwise return False.'''
      
# word = input("Enter the word: ").lower()
# word = word.split(' ')
# word = "".join(word)
# new_word =""

# for val in word[::-1]:
#    new_word = new_word + val
# if word == new_word:
#    print("is palindrome")
# else:
#    print("not a palindrome")


'''*List and String - Reversing Words in a Sentence*
Description: Write a function reverse_words(sentence) that takes a string sentence and returns a new string with the words in reverse order.
reverse_words("Hello World")  # Output: "World Hello"
reverse_words("Python is fun")  # Output: "fun is Python"
*Steps:*
Split the sentence into a list of words.
Reverse the list of words.
Join the reversed list back into a string.
Return the resulting string.'''

# word = input("Enter a sentence: ")
# word = word.split(" ")
# word = " ".join(word[::-1])
# print(word)

'''*String and List - Extracting Numbers from a String*
Description: Write a function extract_numbers(s) that takes a string s containing both letters and numbers, and returns a list of numbers extracted from the string.
extract_numbers("abc123xyz456")  # Output: [123, 456]
extract_numbers("1a2b3c")  # Output: [1, 2, 3]
*Steps:*
Initialize an empty string to accumulate digits and a list to store numbers.
Loop through each character in the string.
If the character is a digit, add it to the current number string.
If the character is not a digit, convert the accumulated number string to an integer and add it to the list.
Return the list of numbers.'''

# value = input("Enter the value: ")
# extract_numbers = []
# num_val = ""
# for char in value:

#    if char.isdigit():
#       num_val += char

#    if char.isdigit() == False and num_val !='':

#       extract_numbers.append(int(num_val))
#       num_val = ""

# if num_val != '':
#     extract_numbers.append(int(num_val))

# print(extract_numbers)




