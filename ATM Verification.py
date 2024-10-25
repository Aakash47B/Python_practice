"""1. Initialize cash_in_machine. (Eg. cash_in_machine=100000)
2. Initialize pin (Eg. pin=1234)
3. Create a while loop.
4. Ask 4 digit Pin number.
5. If entered pin wasn't correct, say "wrong pin" and ask the pin again (up to 3 times)
6. If pin entered as incorrect for 3 times, Say "Transaction Failed, Exceeded maximum pin attempts" for the current user and (Loop will be continued) Ask pin number for the next user.
7. If entered pin was correct, then ask amount needed.
8. If amount needed is available in the machine, Say "Transaction successful, collect your cash"
9. If amount needed isn't available in the machine, Say "Not enough cash in the machine"
10. Continue the loop until Cash_in_machine=0."""

#database
database = [12345,23456,98765] # Valid card numbers
db_list = [[1234,"Babu",2],[1234,"Ramesh",3],[1234,"Ambani",3]] #[pin, username, number of attempts]
# 12345 = [1234,"Babu",2] index:0
# 23456 = [1234,"Ramesh",3] index:1
# 98765 = [1234,"Ambani",3] index:2

# cash available in machine
cash_in_machine = 100000

while cash_in_machine > 0:
   print("=================================================")
   card_num = int(input("Enter your card: "))

   if card_num not in database: # if the entered card number is valid
      print("Card invalid or Expired")
      continue
   
   data_index = database.index(card_num) #Fetch the index of the card number to access corresponding user data
   db_pin_num,username,no_of_attempts = db_list[data_index]
   # db_pin_num = db_list[data_index][0]
   # username = db_list[data_index][1]
   # no_of_attempts = db_list[data_index][2]


   if no_of_attempts == 0: # Check if the card is blocked due to too many incorrect attempts
      print("Card blocked for multiple incorrect pin attempts. Visit bank to rectify.")
      continue
   
   pin = int(input("Enter pin: "))
   if pin != db_pin_num:
      db_list[data_index][2] -= 1 
      print(f"Invalid pin. No. of attempts for this account: {db_list[data_index][2]}")
      continue
   
   print("=================================================")
   print(f"cash available: {cash_in_machine}")
   print(f"Welcome user: {username}")
   withdraw = int(input("Enter the amount to withdraw: "))
   
   if cash_in_machine >= withdraw:
      print("Transaction successful, collect your cash")
      cash_in_machine -= withdraw
   else:
      print("Not enough cash in the machine.")
   print("=================================================")

else:  # If the loop ends, notify that the machine is out of cash
   print("Machine out of cash.")





