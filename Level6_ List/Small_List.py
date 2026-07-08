## Write a program to find the smallest element in a list.
numbers = [10, 25, 8, 40, 15]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print("Smallest element is:", smallest)