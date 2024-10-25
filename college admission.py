"""We have 3 colleges - each college has a different cut off mark for engineering college admission.
Get the 5 marks from the student. Calculate the average. Find out which colleges the student is eligible to get admission.
For eg, College 1 cut off - 93%, College 2 - 89% and college 3 - 97%. If the student's avg is, 94%, the student is eligible
 for admission in College 1 and College 2."""

#Get the 5 marks from the student.
mark1 = float(input("Mark 1: "))
mark2 = float(input("Mark 2: "))
mark3 = float(input("Mark 3: "))
mark4 = float(input("Mark 4: "))
mark5 = float(input("Mark 5: "))

average_mark = (mark1 + mark2 + mark3 + mark4 + mark5) / 5  #finding average to compare

#We have 3 colleges - each college has a different cut off mark for engineering college admission.
college1_cutoff = 93
college2_cutoff = 89
college3_cutoff = 97

eligible_colleges = [] #to store which college are elligible to apply

if average_mark >= college1_cutoff:
   eligible_colleges.append("College 1")

if average_mark >= college2_cutoff:
   eligible_colleges.append("College 2")

if average_mark >= college3_cutoff:
   eligible_colleges.append("College 3")

print(f"The student's average mark is: {average_mark}")

if len(eligible_colleges) == 0: #if no colleges
   print("The student is not eligible for admission in any of the colleges.")

else: #if got eligible 
   print("The student is eligible for admission in the following colleges:")
   for college in eligible_colleges:
      print(college)