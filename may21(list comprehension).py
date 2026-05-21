#LIST COMPREHENSION
'''
a=['codegnan','python','course']
b=str(a)
print(b.upper())
'''
#SYNTAX FOR LIST COMPREHENSION
#a=[expr for var in collection/range]
'''
a=['codegnan','python','course']
b=[i.upper() for i in a]
print(b)
'''
'''
a=['vja','hyd','vzg']
b=[i.capitalize() for i in a]
print(b)
'''
'''
a=[2,4,6,7,8,12,13]
b=[i**2 for i in a]#(i*i) or pow(i,2)
print(b)
'''

#even
'''
a=[i for i in range(16)]
print(a)
'''
#even(if-usage)
'''
a=[i for i in range(16) if i%2==0]
print(a)
'''
#odd(if-usage)
'''
a=[i for i in range(16) if i%2!=0]
print(a)
'''
#task
'''
fruits=['apple','grapes','mango','kiwi','dragon','berry']
a=[i for i in fruits if 'a' in i]
print(a)

fruits=['apple','grapes','mango','kiwi','dragon','berry']
a=[i for i in fruits if 'a' not in i]
print(a)
'''
#if-else in list comprehension
'''
a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)
'''
#task
'''
a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(len(a))]
print(c)
'''
