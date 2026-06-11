#OOPS
#syntax
'''
class classname():    #() can or can't be placed
    name='star'
    age=19
    city='vjw'
    def func_name(method_name):
        print('Statements')
obj=classname()
print(dir(a))
obj.func_name()'''

#class declaration
'''
class Details():
    name='star'
    age=19
    city='vjw'
    def display(self):
        print(self.name,self.age,self.city)
obj=Details()
obj.display()
'''

#object instatiation- creating an object at instant
'''
class Details():
    def Data(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.Data('star',19,'vjw')
a.display()
a.Data('moon',18,'hyd')
a.display()
b=Details()
b.Data('earth',17,'vzg')
b.display()
'''

#object intialization- with constructor
'''
class Details():
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)
obj=Details('star',19,'vjw')
obj.display()
'''
#run-time
'''
name=input('Enter name: ')
age=int(input('Enter age: '))
city=input('Enter city: ')
class Details():
    def __init__(self,name,age,city):    #if run-time input is given then only self must be there in args
        self.name=name   # input('name')
        self.age=age     # int(input('age'))
        self.city=city   # input('city')
    def display(self):
        print(self.name,self.age,self.city)
obj=Details(name,age,city)     #or obj=Details(input('name'),int(input('age')),input('city'))
obj.display()
'''
