"""##buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user. Also get the total number of choc and cakes that the shop has
#Hint - you can buy choc/Cake only if shop has it.

#find how many choc and cake the user can buy."""

#shop stocks
cake_available = 10
chocolate_available = 40

#item prices
cake_price = 150
chocolate_price = 200

#shopping bag
cake_purchased = 0
chocolate_purchased = 0

budget = float(input("Enter your budget: "))
user_total_budget = budget

while True:
   print("===============================================")
   print(f"Your current budget is {budget}")
   preference = input("What would like to buy cake or chocolate: ")

   if preference == "cake":
      if cake_available == 0:
         print("Sorry we are out of stock")
         continue

      else:
         print("=========================================")
         print(f"We have {cake_available} cakes available.")
         print(f"With your current budget you can buy {int(budget//cake_price)} cakes.")
         cake_count = int(input("How many cakes do you like to buy: "))
         cake_count_cost = cake_count * cake_price
         
         if cake_count > cake_available:
            print("We dont have that many cakes available.")
            continue
         
         elif cake_count_cost > budget:
            print("You budget is low.")
            continue
         
         else:
            budget = budget - cake_count_cost #updating budget, cake count and amount of cakes purchased.
            cake_available = cake_available - cake_count
            cake_purchased = cake_purchased + cake_count
            print("=========================================")
            billing = input("Have you bought all the things you need. Type (yes/no): ")
            if billing == "yes":
               break
            else:
               continue

   if preference == "chocolate":
         if chocolate_available == 0:
            print("Sorry we are out of stock")
            continue

         else:
            print("=========================================")
            print(f"We have {chocolate_available} chocolates available.")
            print(f"With your current budget you can buy {int(budget//chocolate_price)} chocolates.")
            chocolate_count = int(input("How many chocolate do you like to buy: "))
            chocolate_count_cost = chocolate_count * chocolate_price
            
            if chocolate_count > chocolate_available:
               print("We dont have that many chocolate available.")
               continue
            
            elif chocolate_count_cost > budget:
               print("You budget is low.")
               continue
            
            else:
               budget = budget - chocolate_count_cost #updating budget, cake count and amount of cakes purchased.
               chocolate_available = chocolate_available - chocolate_count
               chocolate_purchased = chocolate_purchased + chocolate_count
               print("=========================================")
               billing = input("Have you bought all the things you need. Type (yes/no): ")
               if billing == "yes":
                  break
               else:
                  continue
   
   else:
      print("Invalid item.")

#BIlling Counter
print("==========Billing Counter==========")
print(f"Your have purchased {cake_purchased} cakes and {chocolate_purchased} chocolates") 
total = (cake_purchased * cake_price) + (chocolate_purchased * chocolate_price)  
print(f"The total amount for the purchase is {total} and the budget you had was {user_total_budget}.")
print(f"Your change is {user_total_budget - total}")




