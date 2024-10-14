#Question 7: Modify the Chaos program so that it accepts two inputs and then prints a table
#with two columns similar to the one shown in Section 1.8.


#File: chaos.py

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a second number between 0 and 1: "))

    print(f"{'input':<15}{x:<20}{y:<20}")
    print("-"*45)
    for i in range(10):
        x = 3.9*x*(1-x)
        y = 3.9*x*(1-x)
        print(f"{'':<8} {x:<20.10f} {y:<20.10f}")
        
main()
