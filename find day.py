day = int(input("Enter the number of the day: "))

if day == 1:
   day = "Sunday"

elif day == 2:
   day = "Monday"

elif day == 3:
   day = "Tuesday"

elif day == 4:
   day = "Wednesday"

elif day == 5:
   day = "Thursday"

elif day == 6:
   day = "Friday"

elif day == 7:
   day = "Saturday"

else:
   day = "Error"

print(f"Today's day you have entered is: {day}")

#Ternary Operator (true value if condition else false value)
print("Sunday" if day == 1 else 
      "Monday" if day == 2 else 
      "Tuesday" if day == 3 else 
      "Wednesday" if day == 4 else 
      "Thursday" if day == 5 else 
      "Friday" if day == 6 else 
      "Saturday" if day == 7 else 
      "Error")