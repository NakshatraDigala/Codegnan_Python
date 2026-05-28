#PRINT vs RETURN
#print
'''
def add(a,b):
    print(a+b)
add(3,4)
'''

#return
'''
def add(a,b):
    return(a+b)
print(add(3,4))
'''

#multipe prints(prints all three c,d,e)
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(3,4)
'''

#multiple returns(returns only the top return value)
'''
def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    return d
    return e  #OR CAN WRITE return c,d,e(prints all three)
print(cal(3,4))
'''

#KEYWORD AND POSITIONAL ARGUMENTS
#example
'''METHOD-1(values inside func)
def Details(id,name,mailid):#values inside func
    id=10
    name='star'
    mailid='s@gmail.com'
    print(id,name,mailid)
#Details()#doesnot print values
Details(id='id',name='name',mailid='mailid')
'''
'''
def Details(id,name,mailid):
    print(id,name,mailid)
Details(id='id',name='star',mailid='@gmail.com')
#postional arguments inside func calling prints id,name,mailid since no values are given
Details(id=20,name='star',mailid='s@gmail.com')
#prints values 20,star,s@gmail.com
Details(20,'star','s@gmail.com')#no coln names
Details('star','s@gmail.com',20)#not in order yet prints in this new order
Details(name='star',mailid='s@gmail.com',id=20)#prints in order of id,name, mailid
'''

#DEFAULT ARGUMENTS
'''
def Grocery(item,price):#both args are empty
    print('Item: %s'%item)
    print('Price: %.2f'%price)
Grocery('sugar',100)
'''
'''
def  Grocery(item='oil',price=100):#both args are filled
    print('Item: %s'%item)
    print('Price: %.2f'%price)
Grocery()
'''
'''
def  Grocery(item,price=100):#nonempty followed by empty
    print('Item: %s'%item)
    print('Price: %.2f'%price)
Grocery('dhal')
'''
'''
def  Grocery(item='salt',price):#empty followed by nonempty-error
    print('Item: %s'%item)
    print('Price: %.2f'%price)
Grocery(500)
'''
#TASK
'''
def Bakery(item,price,qty):#both args are empty
    print('Item: %s'%item)
    print('Price: %.2f'%price)
    print('Quantity(kg):%f'%qty)
Bakery('BlackForest',1000,1)
'''
'''
def Bakery(item='Caramel',price=2000,qty=1.5):#both args are filled
    print('Item: %s'%item)
    print('Price: %.2f'%price)
    print('Quantity(kg):%f'%qty)
Bakery()
'''
'''
def Bakery(item,price=2000,qty=1.5):#nonempty followed by empty
    print('Item: %s'%item)
    print('Price: %.2f'%price)
    print('Quantity(kg):%f'%qty)
Bakery('Redvelvet')
'''
'''
def Bakery(item='Blueberry',price=2000,qty):#empty followed by nonempty-error
    print('Item: %s'%item)
    print('Price: %.2f'%price)
    print('Quantity(kg):%f'%qty)
Bakery(1.5)
'''

#TASK
#Split Bill
'''
def splitbill():
    a=int(input('Enter total bill: '))
    b=int(input('Total no of people: '))
    print(a/b)
splitbill()
'''
#.format(),fstring
'''
def splitbill():
    a=int(input('Enter total bill: '))
    b=int(input('Total no of people: '))
    print(f'Each individual amount is: {a/b}')
splitbill()

def splitbill():
    a=int(input('Enter total bill: '))
    b=int(input('Total no of people: '))
    print('Each individual amount is:{}'.format(a/b))
splitbill()
'''

