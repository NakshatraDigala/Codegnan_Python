#APPLICATION ON TOPICS TILL NOW
#ATM

account=100000
while True:
    card=input('Insert the card: ')
    if card=='HDFC':
        print('Welcome Nakshatra')
        pwd=int(input('Enter password: '))
        if pwd==1234:
            c=int(input('Choose action to do: 1.Balance  2.Withdraw'))
            if c==1:
                print(f'Current balance is: {account}')
            elif c==2:
                withdrawal_amount=int(input('Enter withdrawal amount: '))
                account-=withdrawal_amount
                print(f'Total balane remaining is {account}')
            else:
                print('Invalid option')
        else:
            print('Invalid password')
    else:
        print('Invalid card')
        
