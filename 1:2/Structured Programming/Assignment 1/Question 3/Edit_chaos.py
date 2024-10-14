# Question 3: Modify the Chaos program using 2.0 in place of 3.9 as the multiplier in the
# logistic function. Your modified line of code should look like this:
# x = 2.0 * x * (1 - x)
# Run the program for various input values and compare the results to those obtained from
# the original program. Write a short paragraph describing any differences that you notice in
# the behavior of the two versions.

#File: chaos.py

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0*x*(1-x) #3.9 was changed to 2.0
        print(x)
main()

'''
Input: 0.075

   x = 3.9 * x * (1 - x)     x = 2.0 * x * (1 - x)
-----------------------------------------------------
1 0.2705625                  0.13875
2 0.7696978910156249         0.238996875
3 0.6913258855687241         0.36375473748046877
4 0.8322381814942397         0.462874456881968
5 0.5445093839538626         0.49724338809638224



Input: 0.53

   x = 3.9 * x * (1 - x)     x = 2.0 * x * (1 - x)
---------------------------------------------------
1 0.9714900000000001         0.4982
2 0.10801900160999972        0.49999352
3 0.3757684979145965         0.4999999999160191
4 0.914809482169457          0.49999999999999994
5 0.303939064658997          0.49999999999999994




Input: 0.2

    x = 3.9 * x * (1 - x)     x = 2.0 * x * (1 - x)
--------------------------------------------------
1 0.6240000000000001     0.32000000000000006
2 0.9150335999999998     0.43520000000000003
3 0.30321373239705673    0.49160192
4 0.8239731430433209     0.4998589445046272
5 0.5656614700878645     0.49999996020669446


When the 3.9 is used as the multiplier, the function produces chaotic behavior where small
changes in the initial value can lead to dramatically different outputs. Using 2.0 as the multiplier
results in more predictable outcomes. As can be seen from the tables above, when the chaotic
function uses the 3.9 multiplier the output quickly diverges. In contrast, with a multiplier of 2.0,
each subsequent value appears to converge and settle around a certain range.
'''
