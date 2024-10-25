# pattern problems
"""1. *
      *  *
      *  *  *
      *  *  *  *  """
# rows = 4  # Number of rows

# for i in range(1, rows + 1):
#     print('*  ' * i)

"""2. *  *  *  *  *
      *  *  *  *
      *  *  *
      *  *
      *             """
# rows = 5
# column = 5
# for i in range(1, rows+1):
#    print('*  ' * column)
#    column -= 1

"""1 2 3 4 5 
   1 2 3 4 5 
   1 2 3 4 5
   1 2 3 4 5
   1 2 3 4 5"""

# num = 5
# for column in range(5):
#    for row in range(1,num+1):
#          print(row ,end=" ")
#    print()


"""* * * * *
   *       *
   *       *
   * * * * *"""

# num = int(input("Enter num: "))
# for column in range(num):
#    for row in range(1,num+1):
#       if row == 1 or row == num or column == 0 or column == num-1:
#          print("*" ,end=" ")
#       else:
#          print(" " ,end=" ")
#    print()

"""* * * * 
   *       *
   *       *
   * * * *  """


# num = 5
# for y in range(1,5):
#    for x in range(1,num+1):
#       if (x == 1 or (x == 5 and y == 2 or x == 5 and y == 3)) or ((y == 1 and x <= 4) or (y == 4 and x <= 4)):
#          print("*" ,end=" ")
#       else:
#          print(" " ,end=" ")
#    print()

"""  * * *  
   *       *
   * * * * *
   *       *   """

# num = 5
# for row in range(1, num):
#    for column in range(1 ,num+1):
#       if ((column == 1 and row != 1) or (column==5 and row != 1)) or (row == 1 and ((column >= 2 and column <= 4)) or row == 3 and ((column >= 2 and column <= 4))):
#          print("*", end=" ")
#       else: 
#          print(" ", end=" ")
#    print()

"""   * * * *  
      *       *
      * * * * 
      *       *
      * * * *      """

# num = 6
# for row in range(1, num):
#    for column in range(1 ,num):
#       if (column == 1 or (column == 5 and (row in [2,4])) or (row in [1,3,5] and column != 5) ):
#          print("*", end=" ")
#       else:
#          print(" ",end=" ")
#    print()


"""
   *
  ***
 *****
*******

"""
# n=4
# for i in range(1,n+1):

#    for j in range(n-i):
#       print(" ",end="")

#    for k in range(1,2*i):
#       print("*",end="")
#    print()


