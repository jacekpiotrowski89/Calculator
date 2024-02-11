import os

def addition():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Addition')
    continue_calc = 'y'
    
    num1 = float(input('Enter the number: '))
    num2 = float(input('Enter the number: '))
    ans = num1 + num2
    values_entered = 2 
    print(f'current result: {ans}')
      
    while continue_calc.lower() == 'y':    
        continue_calc = (input("More addition(y/n)? "))
        
        while continue_calc.lower() not in ['y','n']:
            print("please enter \'y\' or \'n\' ")
            continue_calc = input("More addition(y/n)? ")    
        if continue_calc.lower() == 'n':
                break
    
        num = float(input('Enter a number: '))
        ans += num
        print(f'current result: {ans}')       
        values_entered += 1    
    return [ans, values_entered]    

def subtraction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Subtraction')
    continue_calc = 'y'

    num1 = float(input('Enter a number: '))
    num2 = float(input('Enter a number: '))
    ans = num1 - num2
    values_entered = 2 
    print(f'current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = input("More subtraction(y/n)? ")
        
        while continue_calc.lower() not in ['y','n']:
            print("please enter 'y' or 'n' ")
            continue_calc = input("More subtraction(y/n)? ")    
        if continue_calc.lower() == 'n':
            break 
        
        num = float(input('Enter a number: '))
        ans -= num
        print(f'current result: {ans}')       
        values_entered += 1
    return [ans, values_entered]

def multiplication():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Multiplication')
    continue_calc = 'y'
    
    num1 = float(input('Enter the number: '))
    num2 = float(input('Enter the number: '))
    ans = num1 * num2
    values_entered = 2 
    print(f'current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = input("More multiplication(y/n)? ")
        
        while continue_calc.lower() not in ['y','n']:
            print("please enter 'y' or 'n' ")
            continue_calc = input("More multiplication(y/n)? ")    
        if continue_calc.lower() == 'n':
            break 
        
        num = float(input('Enter a number: '))
        ans *= num
        print(f'current result: {ans}')       
        values_entered += 1
    return [ans, values_entered]

def division():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Division')
    continue_calc = 'y'

    num1 = float(input('Enter the number: '))
    num2 = float(input('Enter the number: '))
    while num2 == 0.0:
        print(':)')
        num2 = float(input('Enter the number: '))
    ans = num1 / num2
    values_entered = 2 
    print(f'current result: {ans}')

    while continue_calc.lower() == 'y':
        continue_calc = input("More division(y/n)? ")
        while continue_calc.lower() not in ['y','n']:
            print("please enter 'y' or 'n' ")
            continue_calc = input("More division(y/n)? ")    
        if continue_calc.lower() == 'n':
            break 
        num = float(input('Enter a number: '))

        while num2 == 0.0:
            print(':)')
            num = float(input('Enter the number: '))

        ans /= num
        print(f'current result: {ans}')       
        values_entered += 1
    return [ans, values_entered]

def calculator():
    quit = False
    while not quit:
        results = []
        print('\nSimple Calculator in Python')
        print('Please Enter:')
        print("'a' for Addiction")
        print("'s' for Subtraction")
        print("'m' for Multiplication")
        print("'d' for Division")
        print("'q' for Quit")

        choice = input('Selection: ')    
    
        if choice == 'q':
            quit = True 
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        elif choice == 'a':
            results = addition()
            print('Ans = ', results[0], 'total input =', results[1])
        elif choice == 's':
            results = subtraction()
            print('Ans = ', results[0], 'total input =', results[1])
        elif choice == 'm':
            results = multiplication()
            print('Ans = ', results[0], 'total input =', results[1])
        elif choice == 'd':
            results = division()
            print('Ans = ', results[0], 'total input =', results[1])
        else:
            print('[Error]: invalid Charakter.')

if __name__ == '__main__':
    calculator()

