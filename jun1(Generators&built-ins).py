#GENERATORS()/[]
'''
a=[i for i in range(10)]#List comprehensions
print(a)
print(type(a))
'''
'''
a=(i for i in range(10))#Generators
#print(a)#prints some random value
print(type(a))
print(*a)#unpacks tuple
'''
'''
a=(i for i in range(10))
#print(list(a))#generator-->list
#print(tuple(a))#generator-->tuple
print(set(a))#generator-->set
'''
'''
a,b=[int(x) for x in input('Enter values: ').split(',')]#two inputs taken at a time
def check(a,b):
    while a<b:
          yield a#doesnot terminate and runs until condition satisfies unlike return
          a=a+1
          yield a#runs a value two times
print(check(a,b))#* to unpack values since this is generator or else it gives random values just like before
#to use this without yield, write print inside while orelse it returns none
'''
'''
a,b=[int(x) for x in input('Enter values: ').split(',')]#two inputs taken at a time
def check(a,b):
    while a<b:
          a=a+1
          return a#only first value of a is returned and the func is terminated
print(check(a,b))#* to unpack values since this is generator
'''

#Diff b/w return and yield
'''
def course():
    return 'python'
    return 'java'
    return 'dsa'
print(course())#returns only first value
'''
'''
def course():
    yield 'python'
    yield 'java'
    yield 'dsa'
print(*course())#* since generator(runs until completion)--prints in one line


#next()
d=course()
print(next(d))#python
print(next(d))#java
print(next(d))#dsa
print(next(d))#error cause three yields are over and no new values are there to print
'''
'''
print(max(2,3,4,5,6,7,8,9))
print(min(2,3,4,5,6,7,8,9))
a=[2,3]#or a=2,3
print(sum(a))
'''

#Build-in func---> use with datatype before asking output(ex in zip())
'''
print(dir())#gives files aka directories
print(dir('__builtins__'))
'''
#fromkeys()-->part of dict
a='code'
'''
print(list(a))#['c','o','d','e']
print(tuple(a))#('c','o','d','e')
print(dict(a))#error cause single value cant be converted into dict

#b=dict.fromkeys(a)
#print(b)

c=dict.fromkeys(a,'value')
print(c)
c['o']='python'#'python' prints as key for o--->c=dict.fromkeys(a,'value')&c['o']='python'  must be in same variable 'c'
print(c)
'''

#eval()---->takes any datatype as input
'''
while True:
    a=eval(input('A value: '))
    b=eval(input('B value: '))
    print(a+b)
    '''

#zip()--->multiple collections to one collections(equal no of values in both collections must be there orelse the extra value will not be paired)
'''
a=[10,20,30,40,50]
b=['one','two','three','four','five']
print(a+b)#prints all in one list
c=zip(a,b)#prints in pairs
print(c)#prints random just like generator so use datatype
#print(list(c))
print(dict(c))#one datatype at a time
'''












