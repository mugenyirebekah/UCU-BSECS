'''
ACTIVITY

1. Write a Python function that checks if a string is the same as the input String
2. Write a Python program to print the multiplication table of a given number up to 12.
3. Write a Python program that finds the largest number in a list without using the max() function.
4. Write a Python program that takes a list of integers as input and returns a list of even numbers.
'''

#ACTIVITY 3

list = [54, 34, 23, 334, 12, 34, 34]

largest = list[0]

for i in list:
    if i > largest:
        largest = i
print(largest)
