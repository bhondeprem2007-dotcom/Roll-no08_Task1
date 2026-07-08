## Write a program to check whether a year is a leap year.

year = int(input("Enter the year"))

try:
    if year % 4 == 0 :
        print("Given Year is Leaf Year")
    elif year > 9999 :
        print("GIven Year is unreal ")
    else:
        print("Given year is not leaf year ")

except : ValueError

