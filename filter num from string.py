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

value = input("Enter the value: ")
extract_numbers = []
num_val = ""
for char in value:

   if char.isdigit():
      num_val += char

   if char.isdigit() == False and num_val !='':

      extract_numbers.append(int(num_val))
      num_val = ""

if num_val != '':
    extract_numbers.append(int(num_val))

print(extract_numbers)