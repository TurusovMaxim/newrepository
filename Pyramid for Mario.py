element = input('Enter the data: ')

def pyramid(element):
    if element.isdigit():
        while int(element) > 23:
            element = input('Enter a number less than 23: ')
        while int(element) < 0:
            element = input('enter a number greater than 0: ')
        if int(element) >= 0 and int(element) <= 23:
            for j in range(int(element)):
                print(' ' * (int(element) - j - 1) + '#' * (j + 2))
    else:
        try:
            float(element)
            while int(element) < 0:
                element = input('Enter a number greater than 0: ')
            while int(element) > 23:
                element = input('Enter a number less than 23: ')
            if int(element) >= 0 and int(element) <= 23:
                for j in range(int(element)):
                    print(' ' * (int(element) - j - 1) + '#' * (j + 2))
        except ValueError:
            element = input('Enter an integer greater than 0 but less than 23: ')
            if int(element) >= 0 and int(element) <= 23:
                for j in range(int(element)):
                    print(' ' * (int(element) - j - 1) + '#' * (j + 2))

print(pyramid(element))
input('Press "enter" for close program ')
