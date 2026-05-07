Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#ARITHMETIC OPERATIONS
a=10
b=29
print(a+b)#Addition
39
print(a-b)#Subtraction
-19
print(a*b)#Multiplication
290
print(a//b)#Integer division(takes only integer part of the result)
0
print(a/b)#Float division
0.3448275862068966
print(a**b)#Power
100000000000000000000000000000
print(a%b)#Reminder
10
#ASSIGNMENT OPERATORS
print(a+=b)#Cant use like this cause = only for variable assigning
SyntaxError: invalid syntax
a
10
b
29
b+=a#b=b+a(updates to latest value everytime)
b#Prints updated value of b
39
b-=a#b=b-a
b
29
b*=a#b=b*a
b
290
b//=a
b
29
b/=a
b
2.9
b**=a#b=b**a
b
42070.72333002009
b%=a#b=b%a
b
0.7233300200896338
#Comparision Operators
a
10
b=20
print(a<b)
True
print(b>a)
True
print(a<=b)
True
print(a>=b)
False
a!=b
True
a==b
False
4<9#Numbers can also be used
True
b==2#Can be used like this also
False
#LOGICAL OPERATORS
a
10
b
20
a>b and a!=b#Both must be true
False
a<b and b>a
True
a<b or a>b
True
not False#Opposite
True
not True#not functions detailed usage will be given later
False
a<b or b==a#Any one must be true
True
#Identify Operations
a
10
if type(a) is int:
    print('It is int')

    
It is int
#Here is and isnot checkes the type of a value
if type(b) is not float:
    print('Is not float')

    
Is not float
#Membership Operators
a=1,2,3,4,5,6
#Here multiple values can be assigned to a single variable
b=7,8,9,10
if 3 in a and b:
    print('true')

    
true
if 3 in a amd 3 in b:
    
SyntaxError: invalid syntax
if 3 in a and 3 in b:
    print('true')

    
#Here condition isnt true so no output
...     
>>> if 4 not in b:
...     print('4 not in b')
... 
...     
4 not in b
>>> #Bitwise Operators
>>> a
(1, 2, 3, 4, 5, 6)
>>> a=10
>>> b
(7, 8, 9, 10)
>>> b=20
>>> a=8;b=4
>>> a&b
0
>>> a=7;b=9
>>> a&b
1
>>> a=3;b=4
>>> a|b
7
>>> a=7;b=8
>>> a|b
15
>>> #Negation
>>> a
7
>>> ¬a
SyntaxError: invalid character '¬' (U+00AC)
>>> ~a
-8
>>> a=5;b=9
>>> a^b
12
>>> a=10;b=2
>>> a^b
8
>>> a<<3
80
>>> a=5
>>> a<<2
20
>>> a=6
>>> a>>2
1
>>> a=3
>>> a>>4
0
>>> a=5
>>> a>>3
0
