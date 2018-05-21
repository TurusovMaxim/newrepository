# Sentences should be entered with a small letter, without spaces or commas
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
                return Vigenere_cipher(element)


def Vigenere_cipher(element):
    """The algorithm for this sort"""
    alphabet = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    key = input('Enter the keyword in Russian too: ')
    cipher = ''
    i = 0
    for c in element:
        amount = alphabet.find(c) + alphabet.find(key[i % len(key)])
        cipher_Vigenere = int(amount) % len(alphabet)
        cipher += alphabet[cipher_Vigenere]
        i += 1
    return print(cipher)

print(data_checking(element))
input('Press any key to end the program ')