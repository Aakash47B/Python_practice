"""count the digits of the num without changing data type"""

# num = -154
# count = 0

# if num < 0:
#    num *= -1
# while num > 0:
#    count += 1
#    num //= 10 
# print(count)

"""count the digits of the num without changing data type and find sum"""

# num = 154
# sum = 0

# while num > 0:
#    rem = num % 10
#    num = num // 10
#    sum += rem 
# print(sum)

'''find odd and even value in the num and filter them and then sum those values as odd sum and even sum'''

num = abs(int(input("Enter num: ")))

odd_sum = 0
even_sum = 0
while num > 0:
   rem = num % 10
   num = num // 10
   
   if rem % 2 == 0:
      even_sum += rem
   else:
      odd_sum += rem


print(f"Odd sum :{odd_sum} and Even sum :{even_sum}")

