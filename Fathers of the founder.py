fathers_of_the_founders = {
    'Niklaus Wirth': 'Pascal',
    'James Gosling': 'Java',
    'Yukihiro Matsumoto': 'Ruby',
    'Guido van Rossum': 'Python',
    'Bjarne Stroustrup': 'C++',
    'Thomas Kurtz': 'Basic'
}
print(fathers_of_the_founders)

print('Enter 0 to sort the dictionary by name')
print('Enter 1 to sort the dictionary by programming language')
print('Enter 2 to find the programming language')
element = input('Enter the data: ')

def data_checking(element):
    """Verification of data entered by the user"""
    if element.isdecimal():
        return fuction_select(element)
    else:
        while True:
            try:
                element = int(input('Enter a number between 0 and 2: '))
                return fuction_select(element)
            except (TypeError, ValueError):
                print('Sorry, but this data is not suitable!')


def fuction_select(element):
    """The choice of the operation to be performed by the user"""
    while int(element) > 2:
        element = input('Enter a number between 0 and 2: ')
    if int(element) < 0:
        element = input('Enter a number between 0 and 2: ')
    else:
        if int(element) == 0:
            return sort_by_name(fathers_of_the_founders)
        if int(element) == 1:
            return sort_by_surname(fathers_of_the_founders)
        if int(element) == 2:
            return search(fathers_of_the_founders)


def sort_by_name(fathers_of_the_founders):
    """Sort the dictionary by the name of the programmer"""
    sorting = sorted(fathers_of_the_founders.items(), key=lambda t: t[0])
    return print(sorting)


def sort_by_surname(fathers_of_the_founders):
    """Sorting the dictionary by programming language"""
    sorting = sorted(fathers_of_the_founders.items(), key=lambda t: t[1])
    return print(sorting)

def search(fathers_of_the_founders):
    """Search for a programming language by the name and surname of the programmer"""
    search = input("Enter the name and surname of the programmer: ")
    for key, value in fathers_of_the_founders.items():
        if key == search:
            print(fathers_of_the_founders[key])

print(data_checking(element))
input('Press "enter" for close program ')