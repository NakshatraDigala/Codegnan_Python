#BREAK
#EXAMPLES
'''
a=10
while a>2:#condition(runs until true)
    print(a)#prints
    a=a-1#decremnet
    if a==5:
        break#break
'''
'''
a=10
while a>2:#condition(runs until true)
    a=a-1#decremnet
    if a==5:
        break#break
    print(a)#prints from 9
'''
'''
for i in range (21):
    if i==14:
        break
    print(i)#0-13
'''
'''
a='python'
for i in a:
    if i=='h':
        break
    print(i)
''' 

#CONTINUE
#EXAMPLES
'''
a=20
while a>10:
    a=a-1
    if a==15:
        continue
    print(a)#19-10 skipping 15
'''
'''
for i in range(15):
    if i==9:
        continue
    print(i)
'''
'''
a='python'
for i in a:
    if i=='h':
        continue
    print(i)
'''

#PASS(holds errors)
#EXAMPLES
'''
a=20
while a>10:
    a=a-1
    if a==15:
        pass
    print(a)
'''
'''
a='python'
for i in a:
    if i=='h':
        pass
    print(i)
'''
