"""The user just bought a few things in your  shop. Ask the user what he bought. 
Cost of one vadai is Rs 30, one soda is Rs20 and one sandwich is Rs 100. Calculate the total cost.
Ask the user to pay the amount. Receive the amount from the user (get money as input). 
Print the change amount you have to give to the user. 
Hint - use float datatype"""



vadai_count = 0
soda_count = 0
sandwich_count = 0

vadai_cost = 0
soda_cost = 0
sandwich_cost = 0

while True:
   print("============================================")
   basket = int(input("What did you buy? (item 1(vadai), item 2(soda), item 3(sandwich)): "))
   if basket == 1:
      count = int(input ("How many vadai: "))
      vadai_count = vadai_count + count
      vadai_cost = vadai_count * 30
   
   if basket == 2:
      count = int(input ("How many soda: "))
      soda_count = soda_count + count
      soda_cost = soda_count * 20
   
   if basket == 3:
      count = int(input ("How many sandwich: "))
      sandwich_count = sandwich_count + count
      sandwich_cost = sandwich_count * 100

   choice = input("Anything else(y/n): ")
   if choice == "n":
      break

total = float(vadai_cost + soda_cost + sandwich_cost)
amount_received = float(input(f"The total amount for the purchase is: {total}. Please pay: "))

print(f"amount paid is {amount_received} and change is {amount_received - total}")




