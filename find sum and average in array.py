'''Find sum of marks in mark array and also find average'''

marks = []

test_taken = int(input("How many marks you are going to add: "))

for test in range(test_taken):
   mark = int(input(f"Enter mark {test+1}: "))
   marks.append(mark)

# To find sum of marks
sum = 0
for test in marks:
   sum = sum + test
print(f"Sum of marks is {sum}")

#to find average of marks
average = sum / test_taken
print(f"Average of marks is {average}")

