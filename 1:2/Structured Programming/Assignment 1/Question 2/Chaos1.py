#Question 2: Enter and run the Chaos program from Section 1.6. Try it out with various
#values of input to see that it functions as described in the chapter.


#File: chaos.py

def main():
    print("this program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9*x*(1-x)
        print(x)
main()



#Results for input value: 0.5
'''
0.975
0.09506250000000008
0.33549992226562525
0.8694649252590003
0.44263310911310905
0.962165255336889
0.1419727793616139
0.4750843861996143
0.9725789275369049
0.1040097132674683
'''



#Results for input value:0.03
'''
0.11349
0.39237907761
0.9298291745493098
0.25446283475440995
0.7398748518843232
0.7505942161905486
0.730089901366194
0.7685286854282509
0.6937801458984842
0.8285520947166924
'''

#Results for input value:0.0002
'''
0.000779844
0.0030390197890090894
0.011816158176151292
0.04553849267021911
0.1695124795866197
0.5490341955189606
0.9656230259122525
0.12946127118723968
0.43953409675431226
0.9607411107242643
'''


''' As the program runs, the value of x seems to jump around chaotically. 
Even though the program has a well defined underlying behavior, the output 
seems unpredictable (just as described in the chapter).'''
