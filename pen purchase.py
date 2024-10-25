pen_price=10
pencil_price=5

item = int(input("What do you want to buy(1:pen, 2:pencil): "))

if item == 1:
      
   pen = input("what color pen do you want blue or black? : ")
   if pen == "blue":
      blue_pen = int(input("How many: "))
      print(f"You have purchased {blue_pen} blue pens and the amount is {blue_pen * pen_price}")
   
   elif pen =="black":
      black_pen = int(input("How many: "))
      print(f"You have purchased {black_pen} black pens and the amount is {black_pen * pen_price}")

   else:
      print("The color you are asking is out of stock")

elif item == 2:
      
   pencil = int(input("How many: "))
   print(f"You have purchased {pencil} pencil and the amount is {pencil*pencil_price}")

else:
   print("The item that you are asking is out of stock")

     





