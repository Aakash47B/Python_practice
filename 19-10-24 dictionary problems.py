"""Contact Book
Create a contact book where the name of the contact is the key, and the value is a dictionary with fields like phone number, email, and address.
Add a few contacts to the dictionary.
Write a program to search for a contact by name and print the details."""

# contact_book = {'David': {'mobile':9876543210, 'email':'david@gmail.com', 'address':'Chennai'},
#                 'Roshan': {'mobile':8976543210, 'email':'roshan@gmail.com', 'address':'Mumbai'},
#                 'Shubam': {'mobile':7986543210, 'email':'shubam@gmail.com', 'address':'Banguluru'}}

# search = input("Enter the name you want to find: ").capitalize()
# details = contact_book.get(search)

# if details != None:
#    for key, value in details.items():
#       print("".join(f"{key}: {value}"))
# else:
#    print("Name does not exist.")

# print("\n".join(f"{key}: {value}" for key, value in details.items()) if details != None else "Name does not exist.")

"""Reverse a Dictionary
Given a dictionary where the values are unique, write a program to reverse the dictionary (i.e., swap the keys with the values).
Input Example:{'apple': 1, 'banana': 2, 'mango': 3} 
Expected Output:{1: 'apple', 2: 'banana', 3: 'mango'}"""

# basket = {'apple': 1, 'banana': 2, 'mango': 3}
# basket = {value: key for key, value in basket.items()}
# print(basket)

"""Grouping Students by Grade
Given a list of students and their grades, write a program to group the students by their grades using a dictionary.
Input Example:
students = [
   {"name": "Alice", "grade": "A"},
   {"name": "Bob", "grade": "B"},
   {"name": "Charlie", "grade": "A"},
   {"name": "David", "grade": "C"}
]
Expected Output:
{'A': ['Alice', 'Charlie'], 'B': ['Bob'], 'C': ['David']}"""

# students = [
#    {"name": "Alice", "grade": "A"},
#    {"name": "Bob", "grade": "B"},
#    {"name": "Charlie", "grade": "A"},
#    {"name": "David", "grade": "C"}
# ]

# class_grades = {}
# for student in students:
#    name = student['name']
#    grade = student['grade']

#    if grade not in class_grades:
#       class_grades.update({grade:[]})
#    class_grades[grade].append(name)

# print(class_grades)   

"""Sort a Dictionary by Values
Write a program that sorts a dictionary by its values in descending order.
Input Example: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92} 
Expected Output: {'David': 92, 'Bob': 90, 'Alice': 85, 'Charlie': 78}"""

# students = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
# marks = sorted(set(students.values()),reverse=True)
# sorted_marks = {}
# for mark in marks:
#    for student in students:
#       if mark == students[student]:
#          sorted_marks.update({student:mark})
# print(sorted_marks)

"""Word Lengths
Write a program that takes a list of words and creates a dictionary where the keys are the words and the values are their lengths.
Input Example: ["apple", "banana", "mango"]
Expected Output: {'apple': 5, 'banana': 6, 'mango': 5}"""

# inputValue = ["apple", "banana", "mango"]
# word_length = {word: len(word) for word in inputValue}
# print(word_length)

"""Find Students with a Specific Grade
Write a program that searches a dictionary of students and prints the names of students who have a specific grade.
Input Example:
students = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}
If the user searches for grade "A", the program should output:
Alice
Charlie"""

# students = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}
# grade = input("Enter the Grade to fetch specific students: ").upper()

# for name, grades in students.items():
#    if grade == grades:
#       print(name)
   
