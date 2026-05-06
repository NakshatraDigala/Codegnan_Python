Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=10
print(a)
10
b=20
print(b)
20
c=30
print(c)
30
X=40
print(X)
40
x==100
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x==100
NameError: name 'x' is not defined. Did you mean: 'X'?
X==100
False
print(X=100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(X=100)
TypeError: print() got an unexpected keyword argument 'X'
>>> print(X==100)
False
>>> a123=100
>>> print(a123)
100
>>> 234=100#variable started with numbers
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a123=10000#variables started with letter and continued with integer
>>> print(a123)
10000
>>> @=1#spl character as variable name
SyntaxError: invalid syntax
>>> _=30#underscore as variable name
>>> print(_)
30
>>>  =90#space as variable name
...  
SyntaxError: unexpected indent
>>> print=100#keyword as variable name
>>> print(print)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(print)
TypeError: 'int' object is not callable
>>> #little experiment of my own:
>>> print(print("Star"))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(print("Star"))
TypeError: 'int' object is not callable
>>> name="Star"#words as variable name
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(name)
TypeError: 'int' object is not callable
>>> Name="Star"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(Name)
TypeError: 'int' object is not callable
>>> NAME="Naks"
>>> print(NAME)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(NAME)
TypeError: 'int' object is not callable
