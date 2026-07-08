##Write a program to find the largest element in a list.


numbers = [10, 25, 8, 40, 15]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest element is:", largest)