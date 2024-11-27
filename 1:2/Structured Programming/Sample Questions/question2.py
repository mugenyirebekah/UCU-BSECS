#Write a Python program to print the multiplication table of a given number up to 12.


def main():
    print("This program prints the multiplication table of a given number up to twelve.")

    n = eval(input("Enter a number: "))

    print()
    print(f"Multiplaction Table for {n}")
    print('-'*30)

    for i in range(1,13):
        print(f"{i} x {n} = {i*n}")

main()
