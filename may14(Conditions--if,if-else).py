#CONDITIONS
#---------------------------if-condition using comparision operators(<,>,<=,>=,!=,==)------------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
'''
#Using <
'''
if a<b:
    print('a value is less than b value')
'''
#Using >
'''
if a>b:
    print('a value is greater than b value')
'''
#Using <=
'''
if a<=b:
    print('a value is less than or equal to b value')
'''
#Using >=
'''
if a>=b:
    print('a value is greater than or equal to b value')
'''
#Using !=
'''
if a!=b:
    print('a value is not equal to b value')
'''
#Using ==
'''
if a==b:
    print('a value is equal to b value')
'''
#(==,!=) on STRING
'''
a=input('Enter the coding language name you are interested in: ')
if a=='python':
    print('You can join a 35 days python course as a sample')
'''
'''
a=input('Enter the coding language name you are interested in: ')
if a!='python':
    print('You can't join a 35 days python course as a sample')
'''


#---------------------------if-condition using logical operators(and,or,not)-------------------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
'''
#Using 'and'
'''
if a>b and b<a:
    print('a is greater than b and b is less than a')
'''
#Using 'or'
'''
if a>10 or b>10:
    print('Either of the values of a and b is greater than 10')
'''
#Using 'not'
'''
if not a!=b and a==b:
    print('a is equal to b')
'''
#(==,!=) on STRING
'''
a=input('Enter your course name: ')
b=input('Enter your year: ')
if a=='cse' and b!=1:
    print('You should take python course')
'''


#---------------------------------if-condition using identify operators(is, is not)----------------------------
'''
a=float(input('Enter a value: '))
'''
#Using 'is'
'''
if type(a) is float:
        print('Type of a is float')
'''
#Using 'is not'
'''
if type(a) is not float:
    print('Type of a is not float')
'''
#(is, is not) on STRING
'''
a=str(input('Data: '))
if type(a) is str:
      print('String type')
'''   


#-------------------------------------if-condition using membership operators(in, not in)-------------------------------
'''
a=int(input('Enter a value: '))
b=[1,2,3,4,5,6,7,8,9,10]
'''
#Using 'in'
'''
if a in b:
    print('a belongs to first 10 integer values')
'''
#Using 'not in'
'''
if a not in b:
    print('a doesnot belongs to first 10 integer values')
'''
#Error case
'''
a=int(input('Enter a value: '))

if 10 in a:
    print('True')#Error(even if a=10) because you cannot restrict user input 'a' to only one value i.e, 10
'''


#--------------------------if-else using comparision operators(<,>,<=,>=,!=,==)------------------------
'''
a=int(input('Enter a age: '))
b=int(input('Enter b age: '))
'''
#Using <
'''
if a<b:
    print('a is younger')
else:
    print('a is not younger')
'''
#Using >
'''
if a>b:
    print('a is elder')
else:
    print('a is not elder')
'''
#Using <=
'''
if a<=b:
    print('a might be of same age or younger')
else:
    print('a is not younger or same age')
'''
#Using >=
'''
if a>=b:
    print('a might be of same age or elder')
else:
    print('a is not elder or same age')
'''
#Using !=
'''
if a!=b:
    print('a and be are not of same age')
'''
#Using ==
'''
if a==b:
    print('a and be are of same age')
'''


#---------------------------if-else condition using logical operators(and,or,not)-------------------------------
'''
a=int(input('Enter a value: '))
b=int(input('Enter b value: '))
'''
#Using 'and'
'''
if a>b and b<a:
    print('a is greater than b and b is less than a')
else:
    print('a is not greater than b and b is not less than a')
'''
#Using 'or'
'''
if a>10 or b>10:
    print('Either of the values of a and b is greater than 10')
else:
    print('Either of the values of a and b is not greater than 10')
'''
#Using 'not'
'''
if not a!=b and a==b:
    print('a is equal to b')
else:
    print('a is not equal to b'
'''


#---------------------------------if-else condition using identify operators(is, is not)----------------------------
'''
a=float(input('Enter a value: '))
'''
#Using 'is'
'''
if type(a) is float:
        print('Type of a is float')
else:
    print('Type of a is not float')
'''
#Using 'is not'
'''
if type(a) is not float:
    print('Type of a is not float')
else:
    print('Type of a is float')
'''


#-------------------------------------if-else condition using membership operators(in, not in)-------------------------------
'''
a=int(input('Enter a value: '))
b=[1,2,3,4,5,6,7,8,9,10]
'''
#Using 'in'
'''
if a in b:
    print('a belongs to first 10 integer values')
else:
    print('a doesnot belongs to first 10 integer values')
'''
#Using 'not in'
'''
if a not in b:
    print('a doesnot belongs to first 10 integer values')
else:
    print('a belongs to first 10 integer values')
'''
