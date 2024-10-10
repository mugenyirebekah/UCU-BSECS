#File: chaos.py

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0*x*(1-x) #3.9 was changed to 2.0
        print(x)
main()
