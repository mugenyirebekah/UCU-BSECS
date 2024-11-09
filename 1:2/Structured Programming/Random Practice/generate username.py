#This program generates usernames_type 1


def main():
    print ("This program will generate a username based on your names: ")

    first = input("What is your first name?")

    last = input("What is your last name?")

    username = first[0]+last

    print("Your username is:", username)

main()
