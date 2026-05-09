Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=12
>>> #Formatting
>>> print("Multiplication of a and b:",a*b)
Multiplication of a and b: 120
>>> #Format method
>>> print("Multiplication of {} and {}:{}".format(a,b,a*b))
Multiplication of 10 and 12:120
>>> #fstring
>>> print(f"Multiplication of {a} and {b}:{a*b}")
Multiplication of 10 and 12:120
>>> #string unpacking(self)
>>> name="star"
>>> a,b,c,d=name
>>> print(a,b,c,d)
s t a r
>>> print(d,c,b,a)
r a t s
>>> a=10
>>> b=20
>>> temp c
SyntaxError: invalid syntax
>>> c=a
>>> a=b
>>> b=c
>>> print(a,b)
20 10
>>> #swapping of two variables(the above and below)
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a,b)
20 10
>>> a=10
>>> b=20
>>> a=a+b
>>> b=a-b#30-20
>>> a=a-b#30-10
>>> print(a,b)
20 10
