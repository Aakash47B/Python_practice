"""5. Write a program to calculate the milege. Ask the user how many litres of petrol they have. 
Ask how many km they have to drive. Calcualte the milege. If the mileage is more than 30km per litre, tell 
the user they have to fill the tank again."""


petrol = int(input("How many litres of petrol do you have: "))
distance = int(input("How many km it takes to reach your destination: "))

mileage = distance / petrol

print(f"Your mileage is {mileage} km per litre")

if mileage > 30:
   print("You have to fill your tank again")

else:
   print("Enough petrol to reach the destination")

