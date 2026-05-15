#CONDITIONS
#---------------------------if-elif-else using comparision operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
'''
'''
if a<b:
    print('a less than b')
elif a>b:
    print('a greater than b')
elif a<=b:
    print('a less than or equal to than b')
elif a>=b:
    print('a greater than or equal to than b')
elif a!=b:
    print('a not equal to b')
elif a==b:
    print('a equal to b')
else:
    print('Invalid input')
'''


#---------------------------if-elif-else using logical operators-----------------------
'''
a=int(input('Enter a value: '))
if a!=10 and a<10:
    print('a is below 10')
elif a!=10 or a>10:
    print('a is equal to or above 10')
elif not a==10:
    print('a not equal to 10')
else:
    print('Invalid input')
'''

#---------------------------if-elif-else using identify operators----------------------
'''
a=int(input('Enter a value: '))
if type(a) is int:
    print('a is Integer type')
elif type(a) is not int:
    print('a is not Integer type')
else:
    print('Invalid input')
'''

#---------------------------if-elif-else using membership operators----------------------
'''
a=int(input('Enter a value: '))
c=[10,20,30,40,50,60,70,80,90,100]
if a in c:
    print('a is one of the first 10 multiples of 10')
elif a not in c:
    print('a is not one of the first 10 multiples of 10')
else:
    print('Invalid input')
'''


#---------------------------multiple-if using comparision operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))

if a<b:
    print('a less than b')
if a>b:
    print('a greater than b')
if a<=b:
    print('a less than or equal to b')
if a>=b:
    print('a greater than or equal to b')
if a!=b:
    print('a not equal to b')
if a==b:
    print('a equal to b')
'''


#---------------------------multiple-if using logical operators-----------------------
'''
a=int(input('Enter a value: '))
if a!=10 and a<10:
    print('a is below 10')
if a!=10 or a>10:
    print('a is equal to or above 10')
if not a==10:
    print('a not equal to 10')
'''


#---------------------------multiple-if using identify operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
if type(a) is int:
    print('a is Integer type')
if type(a) is not int:
    print('a is not Integer type')
if type(b) is int:
    print('b is Integer type')
if type(b) is not int:
    print('b is not Integer type')
'''


#---------------------------multiple-if using membership operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
c=[10,20,30,40,50,60,70,80,90,100]
if a in c:
    print('a is one of the first 10 multiples of 10')
if a not in c:
    print('a is not one of the first 10 multiples of 10')
if b in c:
    print('b is one of the first 10 multiples of 10')
if b not in c:
    print('b is not one of the first 10 multiples of 10')
'''

#---------------------------nested-if using comparision operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
if a<b:
    print('a is less than b')
    if a==b:
        print('a is less than and equal to b')
if a>b:
    print('a is greater than b')
    if a==b:
        print('a is greater than and equal to b')
if a!=b:
    print('a is not equal to b')
'''


#---------------------------nested-if using logical operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
if a>10 or a==10:
    print('a greater than or equal to 10')
    if a!=b and not a>b:
        print('a is greater than b')
'''


#---------------------------nested-if using identify operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
if type(a) is int:
    print('a is Integer type')
    if type(b) is not float:
        print('b is Integer type')
'''


#---------------------------nested-if using membership operators-----------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
c=[10,20,30,40,50,60,70,80,90,100]
if a in c:
    print('a is one of the first 10 multiples of 10')
    if b not in c:
        print('b is not one of the first 10 multiples of 10')
    else:
        print('b is one of the first 10 multiples of 10')
'''





