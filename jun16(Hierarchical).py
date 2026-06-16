#Hierarchical-- single parent class is inherited by multiple child classes
'''
class Employee():   #parent class
    def work(self):
        print('IT solutions')
class Trainer(Employee):    #child-1
    def teaching(self):
        print('Trainer teaches')
class Developer(Employee):     #child-2
    def developing(self):
        print('Developer develops')
a=Trainer()
b=Developer()
a.work()   #calls parent class func since it is inherited
a.teaching()
b.work()
b.developing()
'''
#Hybrid Inheritance  - both hierarchical and multiple
'''
class Person():
    def details(self):
        print('Details of a person/Name')
class Teacher(Person):   #Hierarchical Inheritance
    def teach(self):
        print('Teacher teaches')
class Student(Person):    #Hierarchical Inheritance
    def study(self):
        print('Student learns')
class Teaching_Assistant(Teacher,Student):     #Multiple Inheritance
    def both(self):
        print('Teaching Assistant assists')
c=Teaching_Assistant()  #calling one class prints all other classes since person class is inherited in Teacher, Student class
#and they both are inherited by Teaching_Assistant
c.details()
c.teach()
c.study()
c.both()
'''
#super()  - inherits a parent variable in child when a constructor is used 

class parent():
    def __init__(self,name):
        self.name=name
        print('Parent constructor')
class child(parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print('Child constructor')
a=child('Star',19)
print(a.name)
print(a.age)
#a.__init__('Moon',19)#--this asks for another input and when input is given, star only comes
