Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#ALL OTHER TYPES->int
int(10)#int->int
10
int(9.08)#float->int
9
int('Star')#str->int
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('Star')#str->int
ValueError: invalid literal for int() with base 10: 'Star'
int(4+5j)#complex->int
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(4+5j)#complex->int
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)#bool->int
1
int(False)#bool->int
0
#ALL OTHER TYPES->float
float(100)
100.0
float(9.08)
9.08
>>> float('Star')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float('Star')
ValueError: could not convert string to float: 'Star'
>>> float('4+5j')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float('4+5j')
ValueError: could not convert string to float: '4+5j'
>>> float(True)
1.0
>>> #ALL OTHER TYPES->str
>>> str(20)
'20'
>>> str(9.08)
'9.08'
>>> str('star')
'star'
>>> str(4+5j)
'(4+5j)'
>>> str(True)
'True'
>>> #ALL OTHER TYPES->BOOL
>>> bool(90)
True
>>> bool(9.08)
True
>>> bool('code')
True
>>> bool(4+5j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> #ALL OTHER TYPES->complex
>>> complex(10)
(10+0j)
>>> complex(9.08)
(9.08+0j)
>>> complex('str')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    complex('str')
ValueError: complex() arg is a malformed string
>>> complex(4+5j)
(4+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
