#	QUESTION 1: Write a Python program that takes a list of integers as input and returns a list of even numbers.


def menu():
    print("This program allows you to create a list of integers and then prints the even numbers of the list.")
    print('-'*90)


def create_list():  #This function enables the user to create the list
    num_list = []

    xStr = input("Enter any number to create a list (Click enter when you are done): ")

    while xStr != "":
        num_list.append(int(xStr))
        xStr = input("Enter any number to create a list (Click enter when you are done): ")

    print("List creation complete!  ", num_list)

    return num_list


def print_even_numbers(num_list):  #This function prints the even numbers from the created list
    
    print("The even numbers from the list are: ")
    for i in num_list:
        if i % 2 == 0:
            print(i)

def main():
    menu()
    num_list = create_list()
    print_even_numbers(num_list)

main()
