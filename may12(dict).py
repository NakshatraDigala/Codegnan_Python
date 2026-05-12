Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={'name':'Star','year':2026,'month':5}
>>> type(a)
<class 'dict'>
>>> #accessing
>>> a['name']
'Star'
>>> a[2026]#here i gave value as index, so returns an error
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[2026]#here i gave value as index, so returns an error
KeyError: 2026
>>> a.keys()
dict_keys(['name', 'year', 'month'])
>>> a.values()
dict_values(['Star', 2026, 5])
>>> a.items()
dict_items([('name', 'Star'), ('year', 2026), ('month', 5)])
>>> #update
>>> a.update({'date':12},{'time':6:35})#error cause ',' tells multiple arguements are passed
SyntaxError: invalid syntax
>>> a.update({'date':12},{'time':6})#error cause ',' tells multiple arguements are passed
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.update({'date':12},{'time':6})#error cause ',' tells multiple arguements are passed
TypeError: update expected at most 1 argument, got 2
>>> a.update({'date':12,'time':6})
>>> a
{'name': 'Star', 'year': 2026, 'month': 5, 'date': 12, 'time': 6}
>>> #set default
>>> a.setdefault('section','A')
'A'
>>> a
{'name': 'Star', 'year': 2026, 'month': 5, 'date': 12, 'time': 6, 'section': 'A'}
>>> #get
>>> a.get('section')
'A'
>>> #copy
>>> b=a.copy()
>>> b
{'name': 'Star', 'year': 2026, 'month': 5, 'date': 12, 'time': 6, 'section': 'A'}
>>> #pop
>>> a.pop()#pop must have arguments
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.pop()#pop must have arguments
TypeError: pop expected at least 1 argument, got 0
>>> a.pop('month')
5
>>> a
{'name': 'Star', 'year': 2026, 'date': 12, 'time': 6, 'section': 'A'}
>>> a.popitem()#this deletes last item in the list
('section', 'A')
a
{'name': 'Star', 'year': 2026, 'date': 12, 'time': 6}
b.clear()
b
{}
#keys same values different
b={'food':'biryani','colour':'black','colour':'yellow'}
b
{'food': 'biryani', 'colour': 'yellow'}
#here latest update of key is taken i.e, yellow
#keys different, values same
b={'food':'biryani','colour':'black','colour1':'yellow'}
b
{'food': 'biryani', 'colour': 'black', 'colour1': 'yellow'}
#single key, multiple values
c=b.copy()
c
{'food': 'biryani', 'colour': 'black', 'colour1': 'yellow'}
c.update({'coupons':[10,20,30]}
         c
         
SyntaxError: '(' was never closed
c.update({'coupons':[10,20,30]})
         
c
         
{'food': 'biryani', 'colour': 'black', 'colour1': 'yellow', 'coupons': [10, 20, 30]}
