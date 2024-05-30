print('===================================================================================')
print('Made By #SoloStudio')
print('<! Notice This calculator does NOT support decimals and fractions in the equation!>')
print('===================================================================================')

def calculator():
    print('Choose an operation to calculate.')
    print('a. ADD')
    print('s. SUBTRACT')
    print('m. MULTIPLY')
    print('d. DIVIDE')

    calculate = input('Enter your operation: ')

    if calculate == 'a':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('The answer is', x + y)
    elif calculate == 's':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('The answer is', x - y)
    elif calculate == 'm':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('The answer is', x * y)
    elif calculate == 'd':
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        if y == 0:
            print('Error: Cannot divide by zero.')
        else:
            print('The answer is', x / y)
    else:
        print('Error: Invalid selection.')

    restart = input('Do you want to perform another calculation? (yes/no): ')
    if restart.lower() == 'yes':
        calculator()
    else:
        print('Calculator has been closed.')

calculator()

#Developed in 2022 - SoloStudio
#SoloStudio
