########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
# inputString = input("Enter word: ")
# i = 0 #counter to track the chars
# newString = ""
# while i < len(inputString):
#    if i < len(inputString) and (i+1 == len(inputString)):
#       newString += inputString[i]
#       break
#    else:
#       newString += inputString[i]+inputString[i+1]#FillinMissingCode (assign the from i, i+1 of inputString)
#       newString += " " #add space
#       i+=2
# #check to add the chars at the end
# #FillinMissingCode
# print(newString)

########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

# myName = input("Enter word: ") #FillinMissingCode
# for letter in range(len(myName)):
#    print(myName[:letter+1])
        

########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

# inputSentence = input("Enter word: ") #FillinMissingCode
# pigLatinKey = 'ay'
# pigLatin = ""
# for word in inputSentence.split(): #gets the word in a sentence
#    #take the first char
#    firstChar = word[0]
#    if len(word) > 1:   #FillinMissingCode - check if the word has more than one char
#       pigLatin += word[1:] + firstChar + pigLatinKey + " "   
#    else:
#       pigLatin += word + pigLatinKey + " "
#    # word = word[1:] + firstChar + pigLatinKey
# print(pigLatin)
        
########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

# inputSentence = #FillinMissingCode
# pigLatinKey = 'ay'
# vowels = ['a','e','i','o','u']

# for word in inputSentence.split(): #gets the word in a sentence
#     #take the first chars until a vowel
#     first_vowel_index = 0
#     #FillinMissingCode - check if the word has more than one char
#     for index, char in enumerate(word): #returns both the index and the char in the word
#          #FillinMissingCode - check if the char is vowel or not
        
     

#     word = #FillinMissingCode  
#     print( #FillinMissingCode)
        

  ########### Program 5 #######
  # Write a program to run a cafe
  #  Cafe should have inventory, sales data and profit
