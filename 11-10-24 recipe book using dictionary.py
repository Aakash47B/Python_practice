"recipe book using dictionary. user asks what food can be made with the item(taken as input) and code give suggestions based on the item"

recipe_book = {
   "Veg": {
         "Paneer Butter Masala": ("Paneer", "Butter", "Tomatoes", "Cream", "Garam masala", "Chili powder"),
         "Palak Paneer": ("Spinach", "Paneer", "Onions", "Tomatoes", "Ginger", "Garlic"),
         "Chole Bhature": ("Chickpeas", "Onions", "Tomatoes", "Ginger", "Garlic", "Chole masala", "Flour", "Yogurt"),
         "Aloo Gobi": ("Potatoes", "Cauliflower", "Onions", "Tomatoes", "Cumin", "Turmeric"),
         "Vegetable Biryani": ("Rice", "Carrots", "Green peas", "Beans", "Onions", "Bay leaf", "Cardamom"),
         "Sambar": ("Toor dal", "Tamarind", "Carrots", "Drumsticks", "Brinjal", "Sambar powder", "Mustard seeds"),
         "Daal Makhani": ("Black lentils", "Butter", "Cream", "Tomatoes", "Ginger", "Garlic"),
         "Vegetable Pulao": ("Rice", "Carrots", "Green peas", "Beans", "Onions", "Bay leaf", "Cardamom"),
   },
   "Non-Veg": {
         "Chicken Biryani": ("Rice", "Chicken", "Yogurt", "Onions", "Garlic", "Ginger", "Bay leaf", "Cardamom"),
         "Butter Chicken": ("Chicken", "Butter", "Tomatoes", "Cream", "Garam masala", "Chili powder"),
         "Fish Curry": ("Fish", "Coconut milk", "Onions", "Tomatoes", "Curry leaves", "Mustard seeds"),
         "Mutton Rogan Josh": ("Mutton", "Yogurt", "Onions", "Garlic", "Ginger", "Garam masala", "Chili powder"),
         "Chicken Tikka Masala": ("Chicken", "Tomatoes", "Cream", "Garam masala", "Chili powder"),
         "Prawn Masala": ("Prawns", "Coconut oil", "Onions", "Tomatoes", "Curry leaves"),
         "Egg Curry": ("Eggs", "Onions", "Tomatoes", "Cumin", "Coriander"),
         "Keema Mutton": ("Mutton", "Onions", "Tomatoes", "Ginger", "Garlic", "Garam masala", "Chili powder"),
   }
}

valid_items = ('Rice', 'Turmeric', 'Tomatoes', 'Garlic', 'Sambar powder', 'Curry leaves', 'Tamarind', 'Mutton', 'Brinjal', 'Yogurt', 'Paneer', 'Cauliflower', 'Garam masala', 'Chicken', 'Mustard seeds', 'Bay leaf', 'Cardamom', 'Spinach', 'Green peas', 'Dal', 'Cream', 'Chickpeas', 'Onions', 'Carrots', 'Black lentils', 'Eggs', 'Ginger', 'Cumin', 'Butter', 'Prawns', 'Potatoes', 'Mutton', 'Drumsticks', 'Chole masala', 'Chili powder', 'Flour', 'Fish', 'Coconut oil', 'Coriander', 'Beans', 'Coconut milk')

def full_recipe():
   recipe_choice = int(input("Enter the number from the suggested: "))
   full_recipe_items = recipe_book.get(preference).get(suggested[recipe_choice - 1])
   print(f"\n{suggested[recipe_choice - 1]}")
   for list_items in full_recipe_items:
      print(list_items)

def suggestions(item,dish_type):
   suggestion = []
   if dish_type == "Veg":
      veg_recipes = recipe_book.get(dish_type)
      for recipe_name,ingredients in veg_recipes.items():
         if item in ingredients:
            suggestion.append(recipe_name)     
      return suggestion
   
   else:
      if dish_type == "Non-Veg":
         Non_Veg_recipes = recipe_book.get(dish_type)
         for recipe_name,ingredients in Non_Veg_recipes.items():
            if item in ingredients:
               suggestion.append(recipe_name)
      return suggestion
      
while True:
   ingredient = input("Welcome to Sunday Samaiyal\nTell the item you have and it give you suggestions\nEnter item: ").capitalize()
   preference = int(input("Veg(1) or Non-veg(2): "))

   preference = "Veg" if preference == 1 else "Non-Veg" if preference == 2 else False
   item_check = True if ingredient in valid_items else False

   if preference != False and item_check == True:
      break

suggested = suggestions(ingredient,preference)

menu_num = 1
print("\nReciples Suggested for the item :")
for menu in suggested:
   print(f"{menu_num}.{menu}")
   menu_num += 1

choice = input("Provide full recipe?(y/n) : ")
if choice == "y":
   full_recipe()