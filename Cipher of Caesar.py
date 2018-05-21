element = input('Please enter any word in Russian: ')

def data_checking(element):
    """Verification of data entered by the user"""
    while element.isdigit():
        element = input('Enter any word in Russian: ')
    else:
        while True:
            try:
                if int(element) < 0:
                    element = input('Enter any word in Russian: ')
            except (TypeError, ValueError):
                return cipher_of_Caesar(element)


def cipher_of_Caesar(element):
    """Algorithm cipher Caesar which moves the letters as the user wants"""
    alphabet = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    k = int(input('Enter a shift from 1 to 32 to encrypt the message: '))
    if k < 1:
        k = 1
    elif k > 32:
        k = 32
    cipher = ''
    for c in element:
        if c in alphabet:
            cipher += alphabet[(alphabet.index(c) + k) % (len(alphabet))]
    return print(cipher)

print(data_checking(element))
input('Press any key to end the program ')