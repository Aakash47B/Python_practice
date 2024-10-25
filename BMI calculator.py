"""#Calculate the BMI and if the person is underweihgt/normal/overweight/obese
#Google how to calculate BMI and decide on the input. The chart below shows the range.
http://www.milkaclarkestrokefoundation.org/uploads/2/4/5/9/2459046/bmi-index_orig.jpg
Use logical and/or conditions."""

#BMI = weight (in pounds) / (height in inches)^2 * 703
#The 703 is needed for converting pounds to kilograms and inches to meters.

# 58 inches (4'10")
# 59 inches (4'11")
# 60 inches (5'0")
# 61 inches (5'1")
# 62 inches (5'2")
# 63 inches (5'3")
# 64 inches (5'4")
# 65 inches (5'5")
# 66 inches (5'6")
# 67 inches (5'7")
# 68 inches (5'8")
# 69 inches (5'9")
# 70 inches (5'10")
# 71 inches (5'11")
# 72 inches (6'0")
# 73 inches (6'1")
# 74 inches (6'2")

height_inches = int(input("Enter your height in inches: "))
weight_lbs = int(input("Enter your weight in lbs: "))
bmi = weight_lbs / (height_inches ** 2) * 703

# Determine weight status
if bmi < 18.5:
   weight_status = "Underweight"

elif bmi >= 18.5 and bmi < 25:
   weight_status = "Normal/Healthy Weight"

elif bmi >= 25 and bmi < 30:
   weight_status = "Overweight"
   
else:
   weight_status = "Obese"

print(f"Your BMI is {int(bmi)} and you are considered {weight_status}.")