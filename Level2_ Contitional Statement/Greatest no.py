## Write a program to find the greatest among three numbers using nested if.

# Input three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Find the greatest using nested if
if a > b:
    if a > c:
        print("Greatest number =", a)
    else:
        print("Greatest number =", c)
else:
    if b > c:
        print("Greatest number =", b)
    else:
        print("Greatest number =", c)
    