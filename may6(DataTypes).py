Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=9
>>> type(a)
<class 'int'>
>>> b=3.456
>>> print(b)
3.456
>>> type(b)
<class 'float'>
>>> c='''this is a string'''
>>> print(type(c))#interpreter can work with and without type
<class 'str'>
>>> #interpreter can work with and without 'print' function
>>> d='p'
>>> type(d)
<class 'str'>
>>> e=4+5j
>>> type(e)
<class 'complex'>
>>> f=5j=7
SyntaxError: cannot assign to literal
>>> f=5j+7
>>> type(f)
<class 'complex'>
>>> x=100j
>>> type(x)
<class 'complex'>
>>> y=7+9i#'i' cant be used as a complex
SyntaxError: invalid decimal literal
>>> y=True#only capital 'T'
>>> type(y)
<class 'bool'>
>>> Y='True'
>>> type(Y)
<class 'str'>
