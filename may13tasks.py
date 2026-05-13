#swapping of two numbers
'''a=10
b=20'''
#method 1(without temp variable)
'''
a,b=b,a
print(a,b)
'''
#method 2(temperary variable)
'''
c=a
a=b
b=c
print(a,b)
'''
#method 3(arithmatic operations)
'''
a=a+b
b=a-b
a=a-b
print(a,b)
'''
#method 4(bit-wise operator XOR)
'''
a=a^b
b=a^b
a=a^b
print(a,b)
'''
#method 5(number formatting)
'''
a=a+b
b=a-b
a=a-b
print('After swapping: a=%d, b=%d' %(a,b))
'''
#String swapping
'''
a='Star'
b='Moon'
temp=a
a=b
b=temp
print('After swapping: a=%s, b=%s' %(a,b))
'''
#Float swapping
''''
a=12.9
b=45
a=a+b
b=a-b
a=a-b
print('After swapping: a=%.2f, b=%d' %(a,b))'''

#task1
'''
a=[9,1,5,2,8,4,6,3,7,0]
b=[]
b=[a[8],a[6],a[5],a[7],a[9],a[0],a[4],a[2],a[3],a[1]]
print(b)#my version1

b=[]
c=[]
b=a[:5]
c=a[5:]
b.sort()
c.sort()
c.reverse()
b.reverse()
print(c+b)#my version2
'''
#task2
'''
a=["codegnan","python","course"]
a1=a[0]
a2=a[1]
a3=a[2]
b1=a1.upper()
b2=a2.upper()
b3=a3.upper()
c=[]
c=[b1,b2,b3]
print(c)#my version

b=str(a)
print(b.upper())#answer
'''
#task3
'''
a=[0,1,2,3,4,5,6]
a.append(10)
print(a)
'''
#task4
'''a=[10,20,30,40]
a.extend([50,'c','o','d','e'])
#a.extend('code')----this also separates c,o,d,e
print(a)
'''
#task5
'''
a=[4,6,7,8,9,10]
a.insert(1,5)
print(a)
'''
#task6
'''
a=(5,6,7,8,9,10,11,12)
a1=list(a)
a1.remove(11)
c=tuple(a1)
print(c)
'''
#task7
'''
a={'year':2026,'month':5}
a.update({'date':13})
print(a)
'''







