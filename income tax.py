"""#Google and find the tax slabs for income tax for India. Write a program to calculate the income tax for an 
#individual. Input is Salary. Optional input - any deductions.
"""
#Tax Slab for FY 2023-24
#https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1


annual_income = float(input("Enter the annual income: "))    

if annual_income <= 300000: #	Up to ₹ 3,00,000 = Nil
   print(f"Your tax to be paid is 'NIL' since your annual income is below or exactly 3,00,000. ")


elif (annual_income > 300000) and (annual_income <= 600000):         #₹ 3,00,001 - ₹ 6,00,000	= 5% above ₹ 3,00,000
   tax_calculation = ((annual_income - 300000) * 5) / 100
   print(f"Total tax for {annual_income} is {tax_calculation}.")


elif (annual_income > 600000) and (annual_income <= 900000):         #₹ 6,00,001 - ₹ 9,00,000	= ₹ 15,000 + 10% above ₹ 6,00,000
   tax_calculation = (((annual_income - 600000) * 10) / 100) + 15000
   print(f"Total tax for {annual_income} is {tax_calculation}.")


elif (annual_income > 900000) and (annual_income <= 1200000):        #₹ 9,00,001 - ₹ 12,00,000	= ₹ 45,000 + 15% above ₹ 9,00,000
   tax_calculation = (((annual_income - 900000) * 15) / 100) + 45000
   print(f"Total tax for {annual_income} is {tax_calculation}.")


elif (annual_income > 1200000) and (annual_income <= 1500000):       #₹ 12,00,001 - ₹ 15,00,000  = ₹ 90,000 + 20% above ₹ 12,00,000
   tax_calculation = (((annual_income - 1200000) * 20) / 100) + 90000
   print(f"Total tax for {annual_income} is {tax_calculation}.")


else:                                                                #Above ₹ 15,00,000	= ₹ 1,50,000 + 30% above ₹ 15,00,000
   tax_calculation = (((annual_income - 1500000) * 30) / 100) + 150000
   print(f"Total tax for {annual_income} is {tax_calculation}.")