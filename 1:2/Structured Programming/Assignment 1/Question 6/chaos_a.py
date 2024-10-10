#QUESTION: The calculation performed in the chaos program can be written 
#in a number of ways that are algebraically equivalent. 
#Write a version of the chaos program for each of the following ways 
#of doing the computation. Have your modified programs print out 100 
#iterations of the function and compare the results when run on the same input.


#(a) 3.9 * x * (1 - x) 

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9*x*(1-x)
        print(x)
        
main()
