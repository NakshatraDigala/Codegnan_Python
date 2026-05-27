#Patterns(HW)
'''
1.Right angle

*
**
***
****
*****
'''
'''
for i in range(1,6):
    print('*'*i)
'''
'''2.Reverse Right angle

*****
****
***
**
*
'''
'''
for i in range(5,0,-1):
    print('*'*i)
 '''   
'''3.Square

****
****
****
****
'''
'''
for i in range(4):
    print('*'*4)
    '''
'''
4.Pyramid

    * 
   * * 
  * * * 
 * * * * 
'''
'''
n=4
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i):
        print('* ',end='')
    print()
'''
#reverse right angled triangle
n=int(input())
for i in range(0,n):
    print('*'*(n-i))

#reverse right angle triangle
n=int(input())
a=n
for i in range(1,n+1):
    print('*'*a)
    a-=1
