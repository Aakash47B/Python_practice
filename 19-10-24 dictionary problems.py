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

# basket = {'apple': 1, 'banana': 2, 'mango': 3,'orange': 1}
# # basket = {value: key for key, value in basket.items()}
# # print(basket)

# reverse_dict = {}
# for key,value in basket.items():
#    if value not in reverse_dict:
#       reverse_dict.update({value:key})
#    else:
#       reverse_dict[value] = [reverse_dict[value], key]      
# print(reverse_dict)

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
#    {"name": "Alice", "grade": 80},
#    {"name": "Bob", "grade": 85},
#    {"name": "Charlie", "grade": 90},
#    {"name": "David", "grade": 95}
# ]

# class_grades = {}
# for student in students:
#    name = student['name']
#    grade = student['grade']

#    if grade not in class_grades:
#       class_grades.update({grade:[]})
#    class_grades.get(grade).append(name)


# print(class_grades)   
# scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# # Define the threshold value
# threshold = int(input("Enter the threshold score: "))

# # Filter the dictionary based on the threshold
# filtered_scores = {name: score for name, score in scores.items() if score > threshold}

# print(filtered_scores)


"""Sort a Dictionary by Values
Write a program that sorts a dictionary by its values in descending order.
Input Example: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92} 
Expected Output: {'David': 92, 'Bob': 90, 'Alice': 85, 'Charlie': 78}"""

# students = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92, 'Davik': 85}
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

# # word_length = {word: len(word) for word in inputValue}

# word_length ={}
# for word in inputValue:
#    word_length.update({word:len(word)})

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
   

# students = {
#     "Alice": {"Math": 85, "English": 78},
#     "Bob": {"Math": 90, "English": 80},
#     "Charlie": {"Math": 70, "English": 65}
# }

# students["Alice"]["Science"]=88
# students["Bob"]["Science"]=78
# students["Charlie"]["Science"]=65

# print(students)

# # Calculate average score for each student
# for student, subjects in students.items():
#     avg_score = sum(subjects.values()) / len(subjects)
#     print(f"{student}'s average score: {avg_score:.2f}")


# def flatten_dict(d, parent_key='', sep='.'):
#     items = {}
#     for key, value in d.items():
#         new_key = f"{parent_key}{sep}{key}" if parent_key else key
#         if isinstance(value, dict):
#             items.update(flatten_dict(value, new_key, sep=sep))
#         else:
#             items[new_key] = value
#     return items

# data = {
#     "name": "Alice",
#     "details": {"age": 25, "address": {"city": "New York", "zip": "10001"}}
# }

# print(flatten_dict(data))



# keys = ['name', 'age', 'city']
# values = ['Alice', 25, 'New York']

# result = dict(zip(keys, values))
# print(result)


# scores = {"Alice": 85, "Bob": 92, "Charlie": 85, "David": 93}
# max_score = max(scores.values())
# print(max_score)

# top_scores = [name for name, score in scores.items() if score == max_score]
# print(top_scores)