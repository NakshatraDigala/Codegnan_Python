#WHILE LOOP
#For numbers
'''
a=10
'''
'''
while a>2:
    print(a)   #this is infinitely prints 10
'''
'''
while a>5:
    print(a)
    a+=3
'''
'''
while a>1:#or can write a>=1 if you want to proint 1 too
    print(a)  #prints from 10
    a=a-1   #if a is greater than the number you take in condition(ex here 1) always do - in this step
'''
'''
while a>1:
    a=a-1   #this prints from 9
    print(a)
'''
'''
while a>1:
    a=a-1   #runs until a doesnot satisfy the contiditon and prints nuber which didnt satisfy the condition
print(a)
'''
'''
while a<30:
    print(a)#10-29
    a+=1
'''
#TASKS
#EVEN OR ODD
'''
while True:   #Can give inputs as many times as possible
    a=int(input('Enter a value: '))
    if a%2==0:
        print('a is even')
    else:
        print('a is odd')
'''
#LEAP YEAR
'''
while True:
    a=int(input('Enter a year: '))
    if a%4==0:
        print('a is a leap year')
    else:
        print('a is not a leap year')
'''

#RANGE LOOP
#start-stop-step
'''
for i in range(15):   #stop
    print(i)
'''

'''
for i in range(5,20):   #start-stop
    print(i)
'''

'''
for i in range(0,30,3):
    print(i,end=' ')
'''

'''
for i in range(2,20,2):
    print(i,end=' ')
'''

'''
for i in range(5,50,5):
    print(i,end=' ')
'''
