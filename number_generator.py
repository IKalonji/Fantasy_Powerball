from random import randint


def number_generator():
    '''Function to return a list of
    numbers which would have been selected 
    by the system which the user woulkd have to guess
    '''

    numbers = []
    powerball = []

    while len(numbers) != 5:

        number = randint(1,50)

        if number in numbers:

            continue

        else:

            numbers.append(number)

    powerball.append(randint(1,20))

    return numbers, powerball


