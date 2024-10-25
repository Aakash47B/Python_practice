"""Try this problem as homework - Check if the username and password is correct. 
     Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
     passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers.
     eg username : myname@sayur.com. password - mnamesay123"""


username = input("Enter your email: ")
password = input("Enter your password: ")


if '@' not in username:  #Username should contain the char @
   print("Invalid email. Does not have @.")

domain = username.split('@')[1]  #Username should contain '.com' or '.edu' or '.tech' or 'org' at the end.
# domain=['myname', 'sayur.com']
# domain[1]

if not domain.endswith('.com') or domain.endswith('.edu') or domain.endswith('.tech') or domain.endswith('.org'):
   print("Invalid domain connection")

company_name = domain.split('.')[0]
#company_name = ['sayur','com']

"""passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
     name of the company mentioned in the username, followed by any 3 numbers."""
#username = myname@sayur.com
expected_passwrd = username[0] + username[2] + username.split('@')[0][-3:] + company_name[:3] + "123"
#expected_password = mnamesay123

if password == expected_passwrd:
   print(f"Welcome User: {username.split('@')[0]}")
else:
   print("Incorrect password")
