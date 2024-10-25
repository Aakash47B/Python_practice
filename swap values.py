"""Write a program that will swap two numbers."""

#using temp
a = 10
b = 20
print("value a",a,"value b",b)

temp = a
a = b
b = temp
print("value a",a,"value b",b)
#============================================
#without temp
a = 10
b = 20
print("value a",a,"value b",b)

b = b-a
a = a+b
print("value a",a,"value b",b)



