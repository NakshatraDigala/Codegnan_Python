Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#LISTS
A=[2,5.6,"PYTHON",5+9j,True]
a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a
NameError: name 'a' is not defined. Did you mean: 'A'?

A
[2, 5.6, 'PYTHON', (5+9j), True]
type(A)
<class 'list'>
#append
a=["python","c","java"]
a.append('ml')
a
['python', 'c', 'java', 'ml']
a.append('c++','ai')#error cause only one argument is allowed
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append('c++','ai')#error cause only one argument is allowed
TypeError: list.append() takes exactly one argument (2 given)
a.append(['c++','ai'])
a
['python', 'c', 'java', 'ml', ['c++', 'ai']]
#extend
a=['python', 'c', 'java', 'ml']
a.extend(['dsa','ai'])#here in output you dont get [] in the list
a
['python', 'c', 'java', 'ml', 'dsa', 'ai']
#insert
a
['python', 'c', 'java', 'ml', 'dsa', 'ai']
a.insert(3,'c++')
a
['python', 'c', 'java', 'c++', 'ml', 'dsa', 'ai']
#INDEX
a
['python', 'c', 'java', 'c++', 'ml', 'dsa', 'ai']
a.index("c")
1
#COPY
c=a.copy()
print(a,c)
['python', 'c', 'java', 'c++', 'ml', 'dsa', 'ai'] ['python', 'c', 'java', 'c++', 'ml', 'dsa', 'ai']
#CLEAR
c.clear()
c#returns empty list
[]
#SORT
a.sort()
a
['ai', 'c', 'c++', 'dsa', 'java', 'ml', 'python']
b=[1,2,3,4.5,4,700]
b.sort()
b
[1, 2, 3, 4, 4.5, 700]
#REVERSE
b.reverse()
b
[700, 4.5, 4, 3, 2, 1]
a.reverse()
a
['python', 'ml', 'java', 'dsa', 'c++', 'c', 'ai']
#POP
a.pop()#deletes last object
'ai'
a.pop(1)
'ml'
#REMOVE
a.remove('java')
a
['python', 'dsa', 'c++', 'c']
#LENGTH
len(a)
4
b=a.copy()+a.extend(['c'])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    b=a.copy()+a.extend(['c'])
TypeError: can only concatenate list (not "NoneType") to list
b=a.copy()
b.extend(['c','java','c++'])
b
['python', 'dsa', 'c++', 'c', 'c', 'c', 'java', 'c++']
b.count('c')
3
len(b)
8
#TUPLE
c=b.copy()
c
['python', 'dsa', 'c++', 'c', 'c', 'c', 'java', 'c++']
d=()
d=c.copy()
d
['python', 'dsa', 'c++', 'c', 'c', 'c', 'java', 'c++']
c=('python', 'dsa', 'c++', 'c', 'c', 'c', 'java', 'c++')
len(c)
8
c.count('c)
        
SyntaxError: unterminated string literal (detected at line 1)
c.count('c')
        
3
c.index(2)
        
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    c.index(2)
ValueError: tuple.index(x): x not in tuple
c.index('java')
        
6
#SETS
        
a={1,3.9,5,6+8j,2,5}
        
type(a)
        
<class 'set'>
b={3.9,5}
        
b.isusbset(a)
        
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    b.isusbset(a)
AttributeError: 'set' object has no attribute 'isusbset'. Did you mean: 'issubset'?
b.isubset(a)
        
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    b.isubset(a)
AttributeError: 'set' object has no attribute 'isubset'. Did you mean: 'issubset'?
        
b.issubset(a)
        
True
a.issuperset(b)
        
True
a.union(b)
        
{1, 2, 3.9, 5, (6+8j)}
a
        
{1, 2, 3.9, 5, (6+8j)}
b
        
{3.9, 5}
a.intersection(b)
        
{3.9, 5}
#UPDATE
        
a
        
{1, 2, 3.9, 5, (6+8j)}
b
        
{3.9, 5}
a.update(b)
        
a
        
{1, 2, 3.9, 5, (6+8j)}
c={100,200,300}
        
b.update(c)
        
b
        
{3.9, 100, 5, 200, 300}
#no old 'b' exists now
        
a.difference(b)
        
{1, 2, (6+8j)}
b.difference(a)
        
{200, 100, 300}
a.symmetric_difference(b)
        
{1, 2, 100, 200, 300, (6+8j)}
b.symmetric_difference(a)
        
{1, 2, 100, 200, 300, (6+8j)}
#DIFFERENCE_UPDATE()
        
a.difference_update(b)
        
a
        
{1, 2, (6+8j)}
a
        
{1, 2, (6+8j)}
b
        
{3.9, 100, 5, 200, 300}
#SYMMETRIC_DIIFERENCE_UPDATE()
        
a.symmetric_difference_update(b)
        
a
        
{1, 2, 3.9, 100, 5, 200, 300, (6+8j)}
a
        
{1, 2, 3.9, 100, 5, 200, 300, (6+8j)}
b
        
{3.9, 100, 5, 200, 300}
b.symmetric_difference_update(a)
        
b
        
{1, 2, (6+8j)}
#INTERSECTION_UPDATE()
        
a
        
{1, 2, 3.9, 100, 5, 200, 300, (6+8j)}
b
        
{1, 2, (6+8j)}
a.intersection_update(b)
        
a
        
{1, 2, (6+8j)}
a={1, 2, 3.9, 100, 5, 200, 300, (6+8j)}
        
b.intersection_update(a)
        
b
        
{1, 2, (6+8j)}
#pop
        
a.pop()
        
1
#remove
        
a.remove(3)
        
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a.remove(3)
KeyError: 3
>>> a.remove(2)
...         
>>> a
...         
{3.9, 100, 5, 200, 300, (6+8j)}
>>> #discard
...         
>>> a.discard(5)
...         
>>> a
...         
{3.9, 100, 200, 300, (6+8j)}
>>> a.index(3)
...         
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a.index(3)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(3.9)
...         
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.count(3.9)
AttributeError: 'set' object has no attribute 'count'
>>> #isdisjoint()
...         
>>> a.isdisjoint(b)
...         
False
>>> i={1,2,3}
...         
>>> j={4,5,6}
...         
>>> i.isdisjoint(j)
...         
True
>>> #clear
...         
>>> i.clear()
...         
>>> i
...         
set()
>>> i.add(100)
...         
>>> i
...         
{100}
