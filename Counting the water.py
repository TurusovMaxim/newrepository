i = int(input('How many minutes do you plan to take a shower? '))

def counting_water(i):
    result = []
    if i > 0:
        result.append(i * 12)
        return result
    else:
        return print('This is not true')

print('To do this you will need',counting_water(i),'bottles')
input('Press "enter" for close program ')