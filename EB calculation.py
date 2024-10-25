units = float(input("Enter the units consumed: ")) 

# Since units are checked in ascending order no need for and operator
if units <= 100:
   unit_cost = 0.0
   print(f"The units consumed is {units} and the electricity bill amount is Rs.{units*unit_cost}")

elif units <= 200:
   unit_cost = 2.35
   print(f"The units consumed is {units} and the electricity bill amount is Rs.{units*unit_cost}")

elif units <= 400:
   unit_cost = 4.70
   print(f"The units consumed is {units} and the electricity bill amount is Rs.{units*unit_cost}")

else: # units more than 500
   unit_cost = 6.30
   print(f"The units consumed is {units} and the electricity bill amount is Rs.{units*unit_cost}")

