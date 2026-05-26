#TASKS
#BMI
'''
weight=float(input('Enter your weight(kg): '))
height=float(input('Enter your height(m): '))
bmi=weight/(height**2)
if bmi==18.5:
    print('Healthy weight')
elif bmi>18.5 and bmi<=24.5:
    print('Normal weight')
elif bmi>24.5 and bmi<=30.0:
    print('Over weight')
elif bmi>=30:
    print('Obesity')
'''

#RAILWAY TICKET
''''
while True:
    gender=input('Enter gender(M/F): ')
    age=int(input('Enter age: '))
    std_price=1000
    if gender=='M':
        if age>60:
            print(f'The ticket price is {std_price-(std_price*(30/100))}')
        else:
            print('The ticket price is ',std_price)
    else:
        if age>60:
            print(f'The ticket price is {std_price-(std_price*(50/100))}')
        else:
            print(f'The ticket price is {std_price-(std_price*(30/100))}')
'''

#ATTENDANCE REPORT
'''
a=int(input('Total no of students: '))
print(f'Total no of students:{a}')
i=0
n=a+1
while i<n:
    b=list(input('Present(P)/Absent(A): '))
    if i==n:
        break
    else:
        i+=1
print(f''No of presentees:{b.count('p')}
            No of absentees:{b.count('a')}'')
'''
#<--wrong approach |||| Correct approach--->

stu=int(input('Total no of students: '))
p=0
ab=0
for i in range(1,stu+1):
    b=input('Present(P)/Absent(A): ')
    c=b.lower()
    if c=='p':
        p+=1
    elif c=='a':
        ab+=1
print(f'''Total no of students:{stu}
            No of presentees:{p}
            No of absentees:{ab}''')
