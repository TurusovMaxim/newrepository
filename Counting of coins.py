element = input('Please enter some amount of money '
                'to get the optimal number of coins: ')

def data_checking(element):
    """Verification of data entered by the user"""
    if element.isdecimal():
        return coin_counting(element)
    else:
        try:
            return coin_counting(element)
        except ValueError:
            element = 0
            while element <= 0:
                try:
                    element = int(input('Enter an integer: '))
                    return coin_counting(element)
                except ValueError:
                    print('Sorry but this is not an integer!')


def coin_counting(element):
    """Algorithm for the selection of optimal coins"""
    while int(element) <= 0:
        element = input('Please enter a number greater than zero: ')
    if int(element) > 0:
        coin_fifty = int(element) // 50
        coin_test = int(element) - 50 * coin_fifty
        coin_ten = coin_test // 10
        coin_test1 = coin_test - 10 * coin_ten
        coin_five = coin_test1 // 5
        coin_test2 = coin_test1 - 5 * coin_five
        coin_one = coin_test2 // 1
    return print('fifty kop:', coin_fifty, ', '
                 'ten kop:', coin_ten, ', '
                 'five kop:', coin_five, ', '
                 'one penn:', coin_one)

# Displays the optimal number of coins
print(data_checking(element))
input('Press "enter" for close program ')