#GLOBAL AND LOCAL VARIABLES
#GLOBAL
#Case-1
'''
a=2
def check1():
    print('a value is:',a)
check1()
print('a value is',a)
'''
#Case-2
'''
a=3
def check2():
    a=5
    a=a**2
    print('Inside value is:',a)
check2()
print('Outside value:'a)
'''
#Case-3
'''
a=4
#b=8
def check3():
    a=6
    print('a value: ',a)
    a=10
    print('a value: ',a+5)
    b=12#local variable
    b=b+10
    print('b value: ',b)
check3()
print('a value: ',a)
print('b value: ',b)#returns error cause b is a local variable
'''
#Case-4(global keyword)
'''
a=4
def check3():
    global a#if this is not given then it returns error cause no value is given before for a
    print('a value: ',a)
    a=10
    print('a value: ',a+5)
    b=12#local variable
    b=b+10
    print('b value: ',b)
check3()
print('a value: ',a)
print('b value: ',b)
'''

#ASCII(chr,ord)
'''
print(chr(38))#chr--->takes only int and returns the alphabet assigned to that number
print(ord('A'))#ord--->takes only char and returns number assigned to that char
'''
#TASK
'''
for i in range(97,123):
    print(chr(i),end=' ')#a-z
for i in range(65,91):
    print(chr(i),end=' ')#A-Z
'''
a=input('Enter your name: ')
print(f'{a}-ASCII value')
for i in a:
    b=ord(i)
    print(f'{i}-{b}',end=' ')#(i,'-',ord(i))
