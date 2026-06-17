#ENCAPSULATION
#public data
'''
class parent():
    publicdata=10   #public data can be accessed by any class's method
    def method1(self):
        print(self.publicdata)
class child(parent):   #parent inherited
    def method2(self):
        print(self.publicdata)  data in parent accessed 
a=child()
a.method2()
a.method1()
'''

#_protecteddata
'''
class parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
a=child()
a.method2()
a.method1()
'''

#__privatedata
'''
class parent():
    __private=100
    def method1(self):
        print(self.__private)
class child(parent):
    def method2(self):
        #print(self.__private)#this is error cause private variables are not called like this
        print(self._parent__private)#already told in diff b/w _&__
        #that __ varibales are called with their class in which they are declared
a=child()
a.method2()
a.method1()
'''
#Abstraction
'''
from abc import ABC,abstractmethod   #ABC is abstract class
class A(ABC):   #imporing abstract class into A class
    @abstractmethod #--this is decoration
    def method1():
        print('python')
a=A()
a.method1()#error cause abstract  methos is not implemented that means method1 doesnot have body anywhere else
'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1():
     pass
    def method2(self):
        print('method2 is implemented')
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print('method1 is implemented')
    def method3(self):
        print('method3 is implemented')
a=B()
a.method1()
a.method2()
a.method3()

    



