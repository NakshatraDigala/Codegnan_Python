'''def greetings(name):
    print('Welcome',name)
a=4
b=5
print(a+b)

d={'id':[1,2,3],'name':['star','moon','earth'],'marks':[10,9,10]}
'''

'''
#def sample():
if __name__=='__main__':#creates a pycache file
    a=[10,20,30,40]
    #a.append('code')#[10,20,30,40,'code']
    a.extend('code')#[10, 20, 30, 40, 'c', 'o', 'd', 'e']
    print(a)
else:
    print('This wont work cause its running as script, not as module')
'''

    
'''      
def dummy():
    if __name__=='__main__':
        print('Script')
    else:
        print('Module')
#dummy()
'''

'''
import math
print(math.pi)
print(math.sqrt(4))
print(math.log(2))
print(math.cos(60))
print(math.acos(-0.9))#these 'a'things like acose etc are mysterious!
print(math.pow(2,4))
print(math.ceil(5.67))
print(math.floor(2.98))
'''


#sys module---to check path and version of python
'''
import sys

print(sys.path)#prints a list
for i in sys.path:
    print(i)#print elements in the list one by one
    
print(sys.version)
'''

#os module
import os
print(os.path)
print(os.getcwd())#get current working directory
print(os.listdir())#lists files
print(os.mkdir('Sample mkdir'))#makes directory just like in command prompt
