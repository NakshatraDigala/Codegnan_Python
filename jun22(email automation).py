#Email automation
#OTP generation
import random
import math
import smtplib#simple mail transfer protocol library

digits='0123456789'#these are the numbers from which OTP must be generated
OTP='' #empty string to store Otp in later
for i in range(6):
     OTP+=digits[math.floor(random.random()*10)]
otp=OTP+' is your OTP'
msg=otp

s=smtplib.SMTP('smtp.gmail.com',587)#server mail id/source mail id
s.starttls()#encrypted mail sending
s.login('nakshatradigala12@gmail.com','wzys wxrl qdle rnqj')
user='nakshatradigala12@gmail.com'
email=input('enter the mail you want to get OTP to')
s.sendmail(user,email,msg)
while True:
    a=input('enter the otp')
    if a==OTP:
        print('OTP is correct')
    else:
        print('Wrong OTP')
