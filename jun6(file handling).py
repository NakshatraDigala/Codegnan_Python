#FILE HANDLING
#write()
'''
a=open('filehandling.txt','w')    #w--overrides info 
a.write('This is write function 1')
a.close()
'''
'''
a=open('filehandling.txt','w')
a.write('This is write function 2')
a.close()
'''

#append()
'''
a=open('filehandling.txt','a')     #a--adds to existing data
a.write('This is write function 3')
a.close()
'''
#runtime
'''
a=open('filehandling.txt','a')
b=str(input('Enter any text'))
a.write(b)
a.close()
'''

#read() types
'''
a=open('filehandling.txt')
#print(a.read())#displays entire file data
#print(a.readline())#displays first line
#print(a.readlines())#displays all data with \n
#print(a.read(10))#displays 10 letters in order
'''

#writelines()--prints side by side
'''
a=open('filehandling.txt','w')
b=['python','java','c++','c','html']
a.writelines(b)#prints side by side
a.writelines('\n'.join(b))#prints one by one in next line
a.close()
'''
#accessing files
'''
a=open('jun6(file handling).py')
print(a.read())
'''
'''
a=open('C:\\Users\\Nakshatra\\Desktop\\Python class IDLE\\filehandling.txt')
print(a.read())
'''

#TASK(Student profile)

stu_id=input('Enter your ID: ')
name=input('Enter your name: ')
phno=int(input('Enter your phno: '))
mail=input('Enter your mailID: ')
clg=input('Enter your college name: ')
branch=input('Enter your branch: ')
print('\n\tStudent Details\n')
print(f'Student ID: {stu_id}\n')
print(f'Student Name: {name}\n')
print(f'Student Phone number: {phno}\n')
print(f'Student Mail ID: {mail}\n')
print(f'Student College Name: {clg}\n')
print(f'Student Branch: {branch}\n')


