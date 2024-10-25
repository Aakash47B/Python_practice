#Fill in the missing code whereever it says #FillinMissingCode
#Fix the syntax errors as needed.

#This is code has functions for basic arithmetic operations. Add, subtract, multiply and divide
#add new functions as needed.

#The main functions is to find the total profit

def addTwoNumbers(n1, n2):
   ans = n1 + n2
   return ans

def subtractAfromB(n1, n2):
   ans = n2 - n1 
   return ans

def multiplyTwoNumbers(n1,n2):
   ans = n1 * n2 
   return ans

def divideAFromB(n1,n2):
   ans = n1 / n2 
   return ans

def sales_per_month(week_sales):
   days_in_month = 30
   sales_per_month = round(multiplyTwoNumbers(week_sales , divideAFromB(days_in_month,7)))
   return sales_per_month

#main code
#we have sales data for a week. 
costOfCoffee, costOfTea, costOfVadai = 25,20,25
total_Coffee_Sales, total_Tea_Sales, total_Vadai_Sales = 0,0,0

#Find total sales in the week.
coffeeSales = [56,78,56,45,90,103,120]    #total:548
for coffee_Sold in range(len(coffeeSales)):
   total_Coffee_Sales = addTwoNumbers(total_Coffee_Sales ,coffeeSales[coffee_Sold])
print(f"Total coffee sold :{total_Coffee_Sales}") 


teaSales = [100,123,456,123,222,400,346]  #total:1770
for tea_Sold in range(len(teaSales)):
   total_Tea_Sales = addTwoNumbers(total_Tea_Sales ,teaSales[tea_Sold])
print(f"Total tea sold :{total_Tea_Sales}") 


vadaiSales = [23,45,67,12,89,90,120]      #total:446
for vadai_Sold in range(len(vadaiSales)):
   total_Vadai_Sales = addTwoNumbers(total_Vadai_Sales ,vadaiSales[vadai_Sold])
print(f"Total vadai sold: {total_Vadai_Sales}")
print("-------------------------------------------------------") 

#calculate avg sales for a week
avg_coffee_sales = round(divideAFromB(total_Coffee_Sales ,len(coffeeSales)))
avg_tea_sales = round(divideAFromB(total_Tea_Sales ,len(teaSales)))
avg_vadai_sales = round(divideAFromB(total_Vadai_Sales ,len(vadaiSales)))
print(f"Average sales of coffee :{avg_coffee_sales}\nAverage sales of tea :{avg_tea_sales}\nAverage sales of vadai :{avg_vadai_sales}")
print("-------------------------------------------------------")
#calculate sales per week
#sales_per_week = addTwoNumbers(addTwoNumbers(multiplyTwoNumbers(total_Coffee_Sales,costOfCoffee), multiplyTwoNumbers(total_Tea_Sales,costOfTea)),multiplyTwoNumbers(total_Vadai_Sales,costOfVadai))
sales_per_week = addTwoNumbers(multiplyTwoNumbers(total_Coffee_Sales,costOfCoffee), multiplyTwoNumbers(total_Tea_Sales,costOfTea))
sales_per_week = addTwoNumbers(sales_per_week,multiplyTwoNumbers(total_Vadai_Sales,costOfVadai))
print(f"Sales per week :₹ {sales_per_week}") #sales_per_week: 60250 

#calcuate sales per month
#258214.2857142857
print(f"Sales per month:₹ {sales_per_month(sales_per_week)}") 
print("-------------------------------------------------------")
#calculate profit.
employeeSalary = 500 #Rs500 per day
totalEmployees = 1
# totalEmployees = int(input("Enter how many employees are working: "))

total_salary_cost_per_week = multiplyTwoNumbers(multiplyTwoNumbers(employeeSalary , totalEmployees) , 7)
profit_per_week = subtractAfromB(total_salary_cost_per_week,sales_per_week)
print(f"Profit for the week: ₹ {profit_per_week}")
print(f"Profit per month:₹ {sales_per_month(profit_per_week)}")
print("-------------------------------------------------------")
 



##Call divide function to get the average from all three subjects
subject1 = 90
subject2 = 86
subject3 = 84

total = addTwoNumbers(subject1,addTwoNumbers(subject2,subject3))
avg = round(divideAFromB(total,3))

print("The avg mark is ", avg)