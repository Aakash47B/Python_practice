"""get two values and find if it is anagram"""

# def anagram(word1,word2): # using sort function
#    if sorted(word1) == sorted(word2):
#       return True
#    else:
#       return False

def anagram(word1,word2):
   if len(word1) != len(word2):
      return False
   
   compare = ""
   for index in range(len(word2)):
      if word1[index] in word2 and word1[index] not in compare:
         compare += word1[index]
      else:
         return False
   return True

s1 = input("Enter word 1: ")
s2 = input("Enter word 2: ")

result= anagram(s1,s2)
print(f"The words \"{s1}\" and \"{s2}\" are anagram." if result==True else f"The words \"{s1}\" and \"{s2}\" are not anagram.")
