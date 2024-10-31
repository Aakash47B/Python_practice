"""1.Merge Multiple Dictionaries with Conflict Resolution
You have multiple dictionaries representing product prices from different stores. If the same product exists in multiple dictionaries, keep the lowest price.
Input:
store1 = {'apple': 3, 'banana': 1, 'mango': 2}
store2 = {'apple': 2, 'banana': 1.5, 'mango': 2.5}
store3 = {'apple': 2.8, 'banana': 1.2, 'mango': 2.3}
Output:
{'apple': 2, 'banana': 1, 'mango': 2}"""

# store1 = {'apple': 3, 'banana': 1, 'mango': 2}
# store2 = {'apple': 2, 'banana': 1.5, 'mango': 2.5}
# store3 = {'apple': 2.8, 'banana': 1.2, 'mango': 2.3}

# stores = [store1,store2,store3]

# merged_prices = {}

# for store in stores:
#    for product, price in store.items():
      
#       # merged_prices.update({product:price}) if product not in merged_prices else merged_prices.update({product:min(merged_prices[product], price)})
      
#       merged_prices[product] = price if product not in merged_prices else min(merged_prices[product], price)

# print(merged_prices)
      
"""2.Group Words by Length
Given a list of words, write a program that creates a dictionary grouping the words by their lengths.
Input:["apple", "banana", "mango", "pear", "peach", "grape"]
Output:
{5: ['apple', 'mango', 'peach', 'grape'], 6: ['banana'], 4: ['pear']}"""

# fruits = ["apple", "banana", "mango", "pear", "peach", "grape"]

# grouped_words = {}

# for fruit in fruits:

#    word_len = len(fruit)
#    if word_len not in grouped_words:
#       grouped_words.update({word_len:[]})
#    grouped_words.get(word_len).append(fruit)

# print(grouped_words)

"""3.Convert a List of Tuples to a Dictionary
Given a list of tuples, write a program to convert it into a dictionary. If a key appears more than once, sum the values associated with that key.
Input:
data = [("apple", 5), ("banana", 3), ("apple", 2), ("banana", 1), ("mango", 4)]
Output:
{'apple': 7, 'banana': 4, 'mango': 4}"""

# data = [("apple", 5), ("banana", 3), ("apple", 2), ("banana", 1), ("mango", 4)]
# result = {}

# for fruit, value in data:
#    result[fruit] = value if fruit not in result else result[fruit] + value

# print(result)

"""4.Find Common Keys in Multiple Dictionaries
Given several dictionaries, write a program to find the common keys among them.
Input:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'c': 7, 'd': 8, 'e': 9}
Output:
{'c'}"""

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
# dict3 = {'c': 7, 'd': 8, 'e': 9}

# for key in dict1:
#    if key in dict2 and key in dict3:
#       print(key)

"""5.Count the Occurrence of Elements in a List Using a Dictionary

Write a program that counts the occurrences of elements in a list and stores them in a dictionary.
Input:[1, 2, 2, 3, 4, 4, 4, 5, 6, 4]
Output:
{1: 1, 2: 2, 3: 1, 4: 4, 5: 1, 6: 1}"""

data = [1, 2, 2, 3, 4, 4, 4, 5, 6, 4]

data = {element : data.count(element) for element in data}

print(data)