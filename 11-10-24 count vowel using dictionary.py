"""Initialize a vowels_count dictonary with zero count values of each vowel. Then count vowels from the given sentence
and update the count in the dictionary. print the dictionary atlast.

eg:
sentence = "I am a student of sayur"
o/p: {'a': 3, 'e': 1, 'i': 1, 'o': 1, 'u': 2}"""

vowels = {'a':0 ,'e':0 ,'i':0 ,'o':0 ,'u':0 }

sentence = input("Enter a sentence: ").lower()
for vowel in vowels:
   count = sentence.count(vowel)
   # vowels[vowel] = count
   vowels.update({vowel:count})

print(vowels)

   

