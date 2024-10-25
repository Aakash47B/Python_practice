# def get_digit(num,pos): #using exponent and not using len function
#    count = 0

#    rem = num % 10**pos
#    temp = rem
#    while temp > 0:
#       temp //= 10
#       count += 1
#    rem = rem // 10**(count-1)
#    return rem

# def get_digit(num,pos): #using exponent and len function
#    rem = num % 10**pos
#    rem = rem // 10**(len(str(rem))-1)
#    return rem

# def get_digit(num,pos): #using iteration
#    iteration=1
#    rem=0
#    while num > 0:
#       rem = num % 10
#       num = num // 10
#       if pos == iteration: break
#       iteration += 1
#    return rem

# def odd_or_even(num):
#    if num % 2 == 0: return "even"
#    else: return "odd"

# def prime(num):
#    for i in range(2, num):
#       if num % i == 0: return False
#    return True
      
# number = int(input("Enter num: "))
# position = int(input("Enter pos: "))

# digit = get_digit(number,position)
# is_odd = odd_or_even(digit)
# is_prime = prime(digit)
# print(f"The num in this position is: {digit}\nThe number is {is_odd}\nIs the num is prime: {is_prime}")

#homework
"""get 2 input one is string of sentence and 2 is position and find if it is vowel"""
# def is_vowel(char):
#    vowel=["a","e","i","o","u"]
#    if char in vowel: return "is a Vowel"
#    else: return "not a Vowel"         overflow: hidden;

# def get_val_using_pos(sentence,pos):
#    index = len(sentence) - pos
#    letter = sentence[index]
#    find = is_vowel(letter)
#    return letter, find
      
# sentence = input("Enter a sentence: ").lower()
# pos = int(input("Enter the position to find: "))

# if pos != 0 and len(sentence) >= pos: 
#    val = get_val_using_pos(sentence,pos)
#    print(f"The word \"{val[0]}\" {val[1]}")
# else:
#    print("Invalid Index")   

