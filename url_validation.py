# '''
# https://www.google.com
# www.google.com
# http://www.google.com
# https://www.annauniv.edu

# www - World Wide Web
# '''
# import sys

# url = input("Enter url to validate: ")
# split_by_dots = url.split('.')
# print(split_by_dots)
# if len(split_by_dots) < 3:
#    print("Invalid url")
#    sys.exit(0)


# if split_by_dots[0].startswith('https://')  or split_by_dots[0].startswith('http://') or split_by_dots[0] == 'www':
#    if split_by_dots[2] == 'com' or split_by_dots[2] == 'edu' or split_by_dots[2] == 'tech'  or split_by_dots[2] == 'org':
#       print("Valid Url")
#    else:
#       print("Invalid url")

# else:
#       print("Invalid url")

'''
https://www.google.com
www.google.com
http://www.google.com
https://www.annauniv.edu

www - World Wide Web
'''

import sys

url = input("Enter url to validate: ")
dot_count = url.count('.')
if dot_count < 2:
   print("Invalid url")
   sys.exit(0)

if url.startswith('https://')  or url.startswith('http://') or url.startswith('www.'):
   if url.endswith('.com') or url.endswith('.edu') or url.endswith('.tech') or url.endswith('.org'):
      print("Valid Url")
   else:
      print("Invalid url")

else:
      print("Invalid url")
