print('Welcome to Python Pizza Deliveries!')
size = input('What size pizza do you want? S M or L: ')
pepero = input('Do you want pepperoni on your pizza? Y or N: ')
cheese = input('Do you want cheese on your pizza? Y or N: ')

bill = 0

if size == 'S':
    bill = 15
    if pepero == 'Y':
        bill += 2
elif size == 'M':
    bill = 20
    if pepero == 'Y':
        bill += 3
elif size == 'L':
    bill = 25
    if pepero == 'Y':
        bill += 3
else:
    print('Fuck you')

if cheese == 'Y':
    bill += 1

print(f'Your final bill is: {bill}')