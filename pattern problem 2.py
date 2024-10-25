"""Print a diamond shape using * symbols. The diamond will have 2n-1 lines, with n lines increasing and then n-1 lines decreasing."""
""" *
   ***
  *****
 *******
  *****
   ***
    *  """
# n=4
# for i in range(1,2*n):

#    if i<=n:
#       for j in range(n-i):
#          print(" ",end="")

#       for k in range(1,2*i):
#          print("*",end="")
#    else:
#       for x in range(i-n):
#          print(" ",end="")
      
#       for y in range(1,2 * (2 * n - i)):
#          print("*",end="")
#    print()

"""Print a Right-Angled Number Triangle
Print a right-angled triangle with numbers in increasing order.

Example: For n = 4: 
1
12
123
1234"""

# num = 4
# for column in range(1,num+1):
#    for row in range(1,column+1):
#       print(row ,end=" ")
#    print()

"""Print a Number Pyramid
Print a pyramid with numbers in each level.

Example: For n = 5:"""
"""
    1 
   2 2 
  3 3 3
 4 4 4 4
5 5 5 5 5
"""

# n=5
# for i in range(1,n+1):

#    for j in range(n-i):
#       print(" ",end="")

#    for k in range(1,i+1):
#       print(i,end=" ")
#    print()

"""Print a Butterfly Pattern
Print a butterfly pattern using * symbols.

Example: For n = 4:"""

# n = 4

# for i in range(1, n + 1): # Upper part

#    for j in range(1, i + 1):
#       print("*", end="")

#    for j in range(2 * (n - i)):
#       print(" ", end="")

#    for j in range(1, i + 1):
#       print("*", end="")
#    print()

# for i in range(n, 0, -1):  # Lower part

#    for j in range(1, i + 1):
#       print("*", end="")

#    for j in range(2 * (n - i)):
#       print(" ", end="")

#    for j in range(1, i + 1):
#       print("*", end="")
#    print()