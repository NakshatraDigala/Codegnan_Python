Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len()
a="python"
len(a)
6
b=''
len(b)
0
c=" "
len(c)#one space=one character
1
#count
a="Johnny johnny yes papa, eating sugar no papa"
a.count("Johnny")
1
a.count('a')
6
#escape sequences
a="name\nmobile no\tmailid"
print(a)
name
mobile no	mailid
b="name:Star\nmobile no:1234567890\tmailid:star@gmail.com"
print(b)
name:Star
mobile no:1234567890	mailid:star@gmail.com
#replace method
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
#find
a.find("i")
2
#upper()
a.upper()
'WAIT UNTIL YOU SUCCEED'
#lower
a.lower()
'wait until you succeed'
a.upper("p")#error:no arguements can be taken inside the upper method
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.upper("p")#error:no arguements can be taken inside the upper method
TypeError: str.upper() takes no arguments (1 given)
#capitalize
a.capitalize
<built-in method capitalize of str object at 0x000001C41AAEFA30>
a.capitalize()
'Wait until you succeed'
#capitalize:only first letter
a.title()#first letter capital in every word
'Wait Until You Succeed'
a[3].upper()
'T'
a
'wait until you succeed'
#is upper
a.isupper()
False
a.islower()
True
a.isdigit()
False
b=890#doesnot work cause it isnt in a string
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b="890"
b.isdigit()
True
c="Star123"
c.isalnum()
True
d="Star@123"
d.isalnum()
False
a.isalpha()
False
#strip(lstrip(),rstrip())
a="     star     "
a.strip()
'star'
a.lstrip()
'star     '
a.rstrip()
'     star'
#split
a="My name is Star"
>>> a.split()
['My', 'name', 'is', 'Star']
>>> #join
>>> a="My","name","is"
>>> a.join()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.join()
AttributeError: 'tuple' object has no attribute 'join'
>>> "".join(a)
'Mynameis'
>>> " ".join(a)
'My name is'
>>> #concatenation
>>> a="star"
>>> b="moon"
>>> print(a+b)
starmoon
>>> print(a+" "+b)
star moon
>>> print(a.title()+""+b.title())
StarMoon
>>> print(a.title()+" "+b.title())
Star Moon
>>> #or
>>> print((a+""+b).title())
Starmoon
>>> print((a+" "+b).title())
Star Moon
>>> #formatting
>>> a=20
>>> b=29
>>> print("The sum is:",a+b)
The sum is: 49
>>> print("The sum is:,{a+b}")
The sum is:,{a+b}
>>> print("The sum is:"{a+b})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("The sum is:",{a+b})
The sum is: {49}
>>> #Format method(here comes what you are doing before)
>>> a="Star"
>>> b="Moon"
>>> print("We have {}{}".format(a,b))
We have StarMoon
>>> print("We have {} {}".format(a,b))#Space between two flower brackets
We have Star Moon
>>> print("We have".format(a,b))
We have
>>> #fstring(here comes what you are doing before)
>>> print(f"We have {a} {b}")
We have Star Moon
