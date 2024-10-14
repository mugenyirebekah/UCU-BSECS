#Loops

#While Loops
#------------


#Example 1
'''age = 19

while(age>18):
    print("You can buy beer")
    age = age+1'''


#Example 2
'''
age =1

while(age<=18):
    print("You can buy beer")
    age = age+1'''


#For loops

'''
for letter in "Danvick":
    print(letter)'''


'''a = 1

while a <=12:
    for i in range (12):
        print(a*(i+1))
    a=a+1'''

'''
for i in range (10):
    pass'''


'''numbers = [1,2,3,4,5,6,7,8,9,10]
    for i in numbers:
        numbers= i/2
        print(numbers)'''



'''numbers = [1,2,3,4,5,6,7,8,9,10]

for i in range(0,10,2):
        print(i)'''


numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if(i%2==0):
        print(i)
