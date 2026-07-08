## Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter the No. : "))

try:
    if num == 0:
        print("Given no. is ZERO")
    
    elif num > 0 :
        print("Given no. is Positive")
    
    else:
        print ("Given no. is NEGATIVE")
    

except: ValueError





