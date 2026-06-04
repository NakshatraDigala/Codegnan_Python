#modules-2
#RANDOM MODULE(generates random digits--real life example:OTP,Ludo game dice)
#sample(range(),)
'''
import random
a=random.sample(range(20,40),5)#5--no of values to be printed//(20,40)---range of numbers to be printed
print(a)
'''
#randint()
'''
import random
a=random.randint(30,40)#prints single number in this range#40 included
print(a)
'''
#choice
'''
import random
a=[10,20,30]
b=random.choice(a)#picks a number from our desired group, here a.
print(b)
'''

#TASK(DICE GAME)
'''
import random
def dice():
    a=random.randint(1,6)
    print('Random dice number:',a)
def chance():
    b=int(input(Want another chance??
            1.Yes  2.No))
    if b==1:
        dice()
    else:
        print('No chance')
c=int(input('Enter any roll of dice(random number): '))
if c<=6:
    dice()
    chance()
else:
    print('Enter a valid number')
'''
'''
import random
a=int(input('Enter any roll of dice(random number): '))
b=random.randint(1,6)
print('Random dice number:',b)

c=int(input(Want another chance??
            1.Yes  2.No))

if c==1:
    b=random.randint(1,6)
    print('Random dice number:',b)
else:
    print('No chance')
'''
'''
import random
a=int(input('Enter any roll of dice(random number): '))
b=random.randint(1,6)
print('Random dice number:',b)

c=int(input(Want another chance??
            1.Yes  2.No))

while c==1:
    b=random.randint(1,6)
    print('Random dice number:',b)
    continue
while c==2:
    break
'''
#optimized solution
'''
import random
a=int(input('Enter any roll of dice(random number): '))
while True:
    b=random.randint(1,6)
    print('Random dice number:',b)

    c=int(input(Want another chance??
                1.Yes  2.No))
    if c==1:
        continue
    else:
        break
'''


#calendar code
'''
import calendar
year=int(input('Enter a year: '))
month=int(input('Enter month: '))
print(calendar.month(year,month))        #prints that year, month calendar
'''
'''
import calendar
year=int(input('Enter a year: '))
print(calendar.calendar(year))              #prints whole calendar of that year
    module     attribute
'''


#date&time
'''
from datetime import date
print(date.today())
'''
'''
import datetime
print(datetime.datetime.now())
#   module      attribute
'''

#epoch time
'''
import time
a=time.time()#prints epoch time(from jan1,1970)
#print(a)

import time
b=time.localtime()#prints local time
#print(b)

import time
#print(f'Today date is:{b.tm_mday}-{b.tm_mon}-{b.tm_year}')

import time
print(f'Exact time is-{b.tm_hour}:{b.tm_min}:{b.tm_sec}')
print(f'Day is: {b.tm_mday}-{b.tm_wday}-{b.tm_isdst}')
'''

#TASK(Random module+time module)
'''
import time
import random
for i in range(1,11):#range(10)
    print(random.randint(1,10))#randint(1000,9999)---OTP generation
    time.sleep(2)
'''


