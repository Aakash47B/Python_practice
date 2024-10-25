"""count duplicate words in the given sentence and store it in dictionary and print the word and its count"""
def count_duplicate(sentence):
   duplicates = {}
   for char in sentence:
      if char.isalpha() == False and char.isspace() == False:
         sentence = sentence.replace(char,"")
   
   sentence = sentence.split(" ")
   
   for word in sentence:
      if word not in duplicates:
         duplicates.update({word:1})
      else:
         count = duplicates.get(word)
         duplicates.update({word:count+1})
   return duplicates

sentence = input("Enter a sentence: ").lower()
duplicates = count_duplicate(sentence)
print(duplicates)

for filtered_words in duplicates:
   if duplicates.get(filtered_words) > 1:
      print(filtered_words)


