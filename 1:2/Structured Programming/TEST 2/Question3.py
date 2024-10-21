#Question 3: Write a Python program that finds the largest number in a list without using the max() function.

numbers = [1,7,3,9,4,8,13,124,57]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("The largest number is", largest)
