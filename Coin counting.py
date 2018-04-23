element = input('Please enter some amount of money to get the optimal change: ')
if element.isdigit():
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
else:
    try:
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
    except ValueError:
        element = input('Please enter an integer: ')
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

print('fifty kop:', coin_fifty, ', ' 'ten kop:', coin_ten, ', ' 'five kop:', coin_five, ', ' 'one penn:', coin_one)
input('Press "enter" for close program ')