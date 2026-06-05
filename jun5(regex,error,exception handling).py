#regex(regular expression)
'''
a='My name is Star'
print(a)

b='My \nname is\n \t Star'
print(b)

#rstring(raw string)
c=r'My \nname is\n \t Star'  #----here escape sequences will not work due to r''
print(c)
'''
#compile(),search(),findall(),split(),sub()----methods in regex
#Sequence characters in regex
'''
\w---matches alphanumeric
\W---non alphanumeric
\d---matches any digit
\D---non-digit
\s---represents white spaces
\S---non-white spaces
'''
#complie()
import re    #re-regular expression
'''a='map mat cat cup money cash maths code noodles'
b=re.compile(r'm\w')#one \w gives two index value outputs
'''
#complie() just runs whats there and doesn't work the logic--
#m->first letter m words-->\w->alphanumeric sequence character
#print(b)


#search()
'''
c=b.search(a)
print(c)#<re.Match object; span=(0, 2), match='ma'>--(0,2):index values-->ma:first two letters in 'map'

d=re.search(r'm\w+',a)
print(d)#<re.Match object; span=(0, 3), match='map'>--\w+: adds a sequence char --prints only one word in search
'''
#findall()
'''
d=re.findall(r'm\w+',a)#prints all m words
print(*d)#map mat money maths
'''

#split()--removes respected elements
'''
e=re.split(r'm',a)#---removes m in a
print(e)#['', 'ap ', 'at cat cup ', 'oney cash ', 'aths code noodles']

e=re.split(r'\s',a)#--\s=white spaces
print(e)#['map', 'mat', 'cat', 'cup', 'money', 'cash', 'maths', 'code', 'noodles']

'''
#sub()--substitutes
'''
x=re.sub(r'm','s',a)
print(x)#sap sat cat cup soney cash saths code noodles
'''

#\d
'''
v='1 cold 3 numb 6 tap water'
u=re.findall(r'\d',v)
print(*u)

y='2007 april 2008 august 2026'
dig=re.findall(r'\d+',y)  # if + given then 2026 wont be split and comes as a whole
print(dig)
'''

#ERROR HANDLING:
#syntax
'''
for i in range(10)
    print(i)#returns syntax error cause : is missing
'''
#runtime error
'''
a=int(input())#if str is given it returns type error
b=int(input())
print(a//b)#if b=0 then it returns value error
'''
#logical error
'''
a=10
b=20
if a>b:    #a>b doesnt satisfy so it stops execution and hence this is logical error where logic is not satisfied
    print('true')
'''

#EXCEPTION HANDLING:
'''
a=int(input('A value: '))
b=int(input('B value: '))
try:       #write a code which has possibilities of errors
    c=a//b
    print(c)
except:         #runs if exception is raised
    print('Input is invalid')
else:     #runs only if try block runs without exceptions
    print('Calculation successful')
finally:         #runs at any costs
    print('End of calculation')
'''














