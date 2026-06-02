#BUILT-INS(PART-2)
#enumerate()--->gives counter to the collection

num=['one','two','three','four','five']
#using for loop
'''
for i in range(len(num)):
    #print(i)#0-4
    print(i,num[i])
'''
#using enumerate
#The diff from enumerate and zip is zip combines two lists but enumerate gives numbers to a single list
'''print(list(enumerate(num)))#prints in pairs
print(list(enumerate(num,100)))#prints from 100
'''

#Anonymous func-namelesss func(keyword-lambda())
#TASK----Calculate 2*x+5 where x=5
'''
def cal(x):
    a=2*x+5
    return a
print(cal(5))
'''
#syntax---a=lambda arg:exp
'''
b=int(input('Enter a value:'))
a=lambda x:2*x+5#Think of this as a func where def replaced by lambda and fun name is 'a'
print(a(b))#here a(value)
'''
#TASK
'''
a='codegnan'
b=lambda x:x.upper()
print(b(a))

a='python course'
b=lambda x:x.title()
print(b(a))
'''
#Str concatenation using lambda
'''
a=input('First name: ')#(or) a,b=[x for X in input('Enter a,b: ').split(',')]--list comprehension    (or)  input('Enter a,b: ').split(',')--won't work for int
b=input('Last name: ')
fullname=a+' '+b
c=lambda a,b:a+' '+b #whatever args you want to give while func calling that only must be given after lambda Ex:a,b in this code
print(c(a,b))
'''
#filter()
'''
a=[3,4,5,7,30,56,45]

if a%2==0:
    print(a)#error:cause a is a list--->for is used to iterate inside the list
    
b=lambda i:i%2==0
c=filter(b,a)#filter b from a
#print(c)#here datatype must be given or else random values come as output
print(tuple(c))
'''
'''
b=[[],(),{},set(),'',4,5.6,'code',5+8j,True,False]
c=list(filter(None,b))#None means empty datatypes are printed
print(c)
'''

#map()---each obj from a collection(lists a,b) and forms new collection
'''
a=[2,4,6,8,10]
b=[3,6,9,12,15]
print(list(map(max,a,b)))#max of a and b(compares index value from a&b)
'''

'''why is this error!!
a=list(map(int,input('Enter a values: ').split(',')))#for list runtime--valuews must be given with separation of commas
b=list(map(int,input('Enter b values: ')))
print(list(map(max,a,b)))
'''
#taking two inputs at a time
'''
a,b=int(input('A value:').split(','))#omly works for str
print(a+b)#ERROR
'''
'''
a,b=[int(x) for x in input('Enter a,b: ').split(',')]#List comprehension
print(a+b)
'''
'''
a,b=map(int,input('A value:').split(',')) #split is given for input, not for map. So close brackets correctly
print(a+b)
'''
'''
a,b=map(eval,input('A value:').split(','))
print(a+b)
'''

b=dict(map(int,input('Enter b values: ').split(',')))
print(b)

