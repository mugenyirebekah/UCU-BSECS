#QUESTION: The calculation performed in the chaos program can be written 
#in a number of ways that are algebraically equivalent. 
#Write a version of the chaos program for each of the following ways 
#of doing the computation. Have your modified programs print out 100 
#iterations of the function and compare the results when run on the same input.

'''
Sample results when run on the same input; using the input 0.8


    3.9 * x * (1 - x)     3.9 * (x - x * x)     3.9 * x - 3.9 * x * x
    -----------------------------------------------------------------
1   0.6239999999999999    0.6239999999999997    0.6239999999999997
2   0.9150336             0.9150336000000004    0.9150336000000001
3   0.303213732397056     0.30321373239705435   0.30321373239705585
4   0.8239731430433197    0.8239731430433173    0.8239731430433195
5   0.5656614700878675    0.5656614700878739    0.5656614700878682
6   0.9581854282490104    0.958185428249007     0.9581854282490099
7   0.1562578420270566    0.156257842027069     0.1562578420270584
8   0.5141811824452056    0.5141811824452389    0.5141811824452105
9   0.9742156868513775    0.9742156868513738    0.9742156868513769
10  0.09796598114189749   0.09796598114191118   0.09796598114189958


The output is similar because the form of the chaotic function has been altered algebraically but
not changed (they are all simply rearrangements of the original function). The imprecision of the
numbers occurs because computers represent real numbers using a finite number of bits. When
performing calculations in an interactive process, small errors accumulate leading to variations in
the results.

'''
