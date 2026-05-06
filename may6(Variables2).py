Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> name="Star"
>>> print(name)
Star
>>> first_name="Star"
>>> print(first_name)
Star
>>> first name="Star"#no space in variable names
SyntaxError: invalid syntax
>>> fname="Star"
>>> lname="d"
>>> print(fname+lname)
Stard
>>> print(fname+" "+lname)
Star d
>>> print(fname,lnmae)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(fname,lnmae)
NameError: name 'lnmae' is not defined. Did you mean: 'lname'?
>>> print(fname,lname)#for space
Star d
>>> a=3,b=4#error occurs
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
>>> a=3;b=4
>>> print(a,b)
3 4
>>> a,b=3,4
>>> print(a,b)
3 4
>>> a=b=c=5
>>> print(a,b,c)
5 5 5
>>> del a#deletes a permenantly
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print(a,b,c)#just checking if it works
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(a,b,c)#just checking if it works
NameError: name 'a' is not defined
>>> if=100#keyword not allowed
SyntaxError: invalid syntax
>>> a=9
>>> a
9
