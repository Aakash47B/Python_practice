"""Create a dictionary with details about a book (title, author, price). Print the values."""
# book = {'title':'Python Programming',
#         'author':'John Doe',
#         'price':'200'}
# print(book)

# student = {1001:{'name':'Ravi','age':23,'major':'CSE'},
#            1002:{'name':'Suman','age':24,'major':'EEE'}}

# print(student)
# for key,value in student.items():
#    print(f'RegNo:{key} - Student details: {value}')

# fruit_stall = {'apple':{'quantity':100,'price':200,'color':'Red'},
#                'orange':{'quantity':81,'price':210,'color':'Orange'}}
# for fruit,details in fruit_stall.items():
#    print(f'Name:{fruit} - Detail: {details}')

# fruit_stall.update({'mango':{'quantity':70,'price':280,'color':'Yellow'}})
# # fruit_stall['orange']['quantity'] = 90
# fruit_stall.get('orange').update({'quantity':90})
# fruit_stall.get('apple').update({'color':'yellow'})
# print(fruit_stall)

import timeit

# Using a for loop
def using_for_loop():
    result = []
    for i in range(5000):
        result.append(i * 2)
    return result

# Using a list comprehension
def using_comprehension():
    return [i * 2 for i in range(1000)]

# Timing the two methods
# loop_time = timeit.timeit(using_for_loop, number=5000)
comprehension_time = timeit.timeit(using_comprehension, number=5000)

# print(f"For loop time: {loop_time}")
print(f"Comprehension time: {comprehension_time}")