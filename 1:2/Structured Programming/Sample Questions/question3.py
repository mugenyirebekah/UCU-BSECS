#Write a Python program that finds the largest number in a list without using the max() function.


def main():
    print("This program finds the largest number in a list.")

    num_list = [1,3,6,9,69, 345, 35]

    largest = num_list[0]

    for i in num_list:
        if i > largest:
            largest = i

    print("The list:", num_list)
    print("The largest number in the list: ", largest)

    
main()

