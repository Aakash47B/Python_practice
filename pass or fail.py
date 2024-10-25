"""1.Get the marks for 3 subjects from the students.

 If the mark is greater than 75 in any two subjects, then print Pass and also print the subject where the marks is > 75
 If the marks is greater than 60 in all three subjects, then print pass.
  If the student scored in 100 in any one subject, it is pass.  Print which subject the student scored 100.
 if the above conditions  not met, print fail."""

subject1 = int(input("Subject 1: "))
subject2 = int(input("Subject 2: "))
subject3 = int(input("Subject 3: "))

if (subject1 == 100 or subject2 == 100 or subject3 == 100): #If the student scored in 100 in any one subject, it is pass.  Print which subject the student scored 100.
   print("Pass")
   if subject1 == 100:
      print("The student scored 100 in Subject 1.")
   elif subject2 == 100:
      print("The student scored 100 in Subject 2.")
   else:
      print("The student scored 100 in Subject 3.")
      
elif(subject1 > 75 and subject2 > 75) or (subject1 > 75 and subject3 > 75) or (subject2 > 75 and subject3 > 75): #comparing 2 subjects 
   print("Pass") #If the mark is greater than 75 in any two subjects, then print Pass
   print("The student scored more than 75 in the following subjects:") #print the subject where the marks is > 75
   if subject1 > 75:
      print("Subject 1")
   if subject2 > 75:
      print("Subject 2")
   if subject3 > 75:
      print("Subject 3")

elif (subject1 > 60 and subject2 > 60 and subject3 > 60): #If the marks is greater than 60 in all three subjects, then print pass.
   print("Pass")


else: #if the above conditions  not met, print fail
   print("Fail")