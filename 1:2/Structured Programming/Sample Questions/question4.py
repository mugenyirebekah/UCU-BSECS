#  Write a Python function that checks if a string is the same as the input String


def main():
    
    print("This checks to see if a string is the same as the input string")
    print('-'*55)

    string = "password123"

    input_string = input("Enter a string: ")

    if string == input_string:
        print("The strings are the same!")

    else:
        print("The strings are not the same!")

    
main()

