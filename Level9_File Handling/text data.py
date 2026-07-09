## Write a program to create and write data into a text file.


file = open("sample.txt", "w")
file.write("Hello, World!\n")
file.write("Welcome to Python file handling.")
file.close()

print("Data written successfully.")