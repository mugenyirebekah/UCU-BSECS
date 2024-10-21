#Question 2: Write a Python program to print the multiplication table of a given number up to 12.

print("This program prints a multiplication table of a given number up to 12")
print("-"*75)

num = eval(input("Enter a number: "))

for i in range(1,13):
	print(f"{num} x {i} = {num*i}")
