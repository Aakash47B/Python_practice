'''
https://www.google.com
www.google.com
http://www.google.com
https://www.annauniv.edu

www - World Wide Web

bugs to fix
1).input is given as "https://.google.com" it should give out as invalid but returns as valid
2).input is given as "https://w.google.com" it should give out as invalid but returns as valid
3).input is given as "https://www..com" it should give out as invalid but returns as valid
4).input given as ""https://www.google.....com hint for loop
5).input given as ""https://.www.google.com it should give out as invalid but returns as valid
'''

import sys

url = input("Enter url to validate: ")
split_by_dots = url.split(".")

protocol = ("https://www","http://www")
domain = (".com",".org",".tech",".edu")

dot_count = url.count('.')

if dot_count > 2:  #if has more than 3 dots in url like https://www.google.....com
   
   if (url.startswith(protocol) == True or split_by_dots[0] == "www") and url.endswith(domain) == True:
               
      paths = split_by_dots[1:-1]  #['google', '', '', '', '']
      for path in paths:
         if path == "":
            print("Invalid url: corrupted url or missing url components")
            sys.exit(0)
      
      print("Valid url")
                  
   else:
      print("Invalid url: Does not satisfy protocol or not starts with 'www' or domain")

elif dot_count == 2:   #if has 2 dots in url like https://www.google.com

   if (url.startswith(protocol) == True or split_by_dots[0] == "www") and url.endswith(domain) == True:

      if split_by_dots[1] == "":
         print("Invalid url: Missing component")
      
      else:
         print("Valid url")
   
   else:
      print("Invalid url: Does not satisfy protocol or not starts with 'www' or domain")

elif dot_count == 1:   #if has  1 dot in url like https://x.com

   if (split_by_dots[0].startswith("https://") or split_by_dots[0].startswith("http://")) and url.endswith(domain) == True:

      slash_position = split_by_dots[0].find("/")
      component = split_by_dots[0][slash_position + 2: ]
      if not component == "":
         print("Valid url")
      
      else:
         print("Invalid url: Missing component")

else: 
   print("Enter valid url")


"""when you use the url.endswith(domain) method, it expects domain to be a single string or a tuple of strings. It checks if the URL string ends with any of the strings in the tuple. If you were to use a list instead of a tuple, you would encounter an error.

Here's why the code works with a tuple:

Tuples are Immutable: Tuples are immutable, meaning their elements cannot be changed. This makes them hashable, and therefore they can be used as keys in dictionaries or as elements in sets.
url.endswith() method: The url.endswith() method expects either a single string or a tuple of strings as its argument. When you pass a tuple of strings, it checks if the URL ends with any of the strings in the tuple.
If you were to use a list instead of a tuple, you would receive a TypeError because lists are mutable and therefore not hashable. Tuples are suitable here because they are hashable and can be used as arguments in methods like url.endswith()

hashable
domain = (".com",".org",".tech",".edu")
[.com][.]-->[.org][.]-->[.tech][.]-->[.edu][.]
"""
