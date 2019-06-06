
def number_ordinal(number):
    if number == 1:
        print('"{}st"'.format(number))
    elif number == 2:
        print('"{}nd"'.format(number))
    elif number == 3:
        print('"{}rd"'.format(number))
    else:
        print('"{}th"'.format(number))

number_ordinal(1)
number_ordinal(2)
number_ordinal(5)

