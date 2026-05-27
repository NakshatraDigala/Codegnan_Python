#FUNCTIONS
#without func
'''
a=11
b=22
print('The sum is: ',a+b)
print('The diff is: ',a-b)
print('The product is: ',a*b)
'''
#with func
'''
def calculate(a,b):#func defining
    print('The sum is: ',a+b)
    print('The diff is: ',a-b)
    print('The product is: ',a*b)
calculate(10,20)#func calling
'''
#run-time input
'''
a=int(input())
b=int(input())
def calculate(a,b):
    print('The sum is: ',a+b)
    print('The diff is: ',a-b)
    print('The product is: ',a*b)
calculate(a,b)
'''
'''
def operations(a,b):
    print('Integer division: ',a//b)
    print('Power: ',a**b)
    print('Modulus: ',a%b)
operations(10,20)
'''
#run-time input(2)
'''
def calculate():#no arguments
    a=int(input())
    b=int(input())
    print('The sum is: ',a+b)
    print('The diff is: ',a-b)
    print('The product is: ',a*b)
calculate()#no arguments
'''
'''
def name():
    a=input('First name: ')
    b=input('Last name: ')
    print((a+' '+b).title())
name()
'''
#TASKS
'''
#single def
a=int(input())
b=int(input())
def operations(a,b):
    c=int(input(Select an option:
                        1.Add
                        2.Sub
                        3.Mul
                        ))
    if c==1:
        print('The sum is: ',a+b)
    elif c==2:
        print('The diff is: ',a-b)
    elif c==3:
        print('The product is: ',a*b)
operations(a,b)
'''
#multiple def

a=int(input('A value: '))
b=int(input('B value: '))
c=int(input('''Select an option:
                        1.Add
                        2.Sub
                        3.Mul
                        '''))
def add(a,b):
        print('The sum is: ',a+b)
def sub(a,b):
        print('The diff is: ',a-b)
def mul(a,b):
        print('The product is: ',a*b)
if c==1:
    add(a,b)
elif c==2:
    sub(a,b)
elif c==3:
    mul(a,b)
else:
    print('Invalid option')


