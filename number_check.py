

def number_check(numbers, powerball, user_numbers, user_powerball):
    '''Function to check correctness of numbers played by the user'''
    
    correct_numbers, correct_powerball = 0,False

    for number in user_numbers:

        if number in numbers:

            correct_numbers += 1

    if powerball == user_powerball:

        correct_powerball = True

    return correct_numbers, correct_powerball