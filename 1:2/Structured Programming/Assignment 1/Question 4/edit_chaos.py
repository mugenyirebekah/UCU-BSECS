# Question 4: Modify the Chaos program so that it prints out 20 values instead of 10.


#File: chaos.py

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9*x*(1-x)
        print(x)
main()
