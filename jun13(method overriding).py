#Method overriding
'''
class Animal():
  def speak(self):
      print('Animals make sounds')
class Dog():
    def speak(self):  #same method name with diff class
        print('Dogs bark')
a=Animal()
d=Dog()
a.speak()
d.speak()
'''
'''
class Bike():
    def vehicle(self):
        print('Royal Enfield')
class Car():
    def vehicle(self):
        print('Porsche')
a=Bike()
b=Car()
a.vehicle()
b.vehicle()
'''

#INHERITANCE
#Single Inheritance
'''
class RBI():
    cash=100000
    def available_cash(cls):
        print('Available cash is: ',cls.cash)
        print('Available cash: ',RBI.cash)
class SBI(RBI):
    pass    #skips this class since RBI doesn't want to give money to SBI
class HDFC(RBI):   #Inserting RBI in child class HDFC allows inheritance
    def new_cash(cls):
        cash=50000
        print('New cash is: ',cls.cash+cls.cash)#when RBI is inherited then cash varibale has value of RBI 
        print('New cash is: ',cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()
'''
#Multiple Inheritance
'''
class Father():
    def weight(self):
        weight=50
        print('Weight is: ',weight)
class Mother():
    def height(self):
        height=5.2
        print('Height: ',height)
class Child(Father,Mother):#Multiple Inheritance
    def dob(self):
        print(f'DOB is: 01-01-2006')
a=Child()   #when inherited you don't need to assign a variable for every class
#and can be called directlywith only child class
a.weight()
a.height()
a.dob()
#can access two parents from child class
'''

#Multi-Level Inheritance
'''
class Grandparents():
    def land(self):
        print('Grandparents give land')
class Parents(Grandparents):
    def house(self):
        print('Parents give house')
class Child(Parents):
    def vehicle(self):
        print('Child gives bike')
a=Child()
a.land()
a.house()
a.vehicle()
'''
