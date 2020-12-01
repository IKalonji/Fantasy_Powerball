import unittest
import number_check

class TestNumberCheck(unittest.TestCase):

    def test_number_check(self):
        '''Testing the number check function
        where powerball is not guessed correctly'''

        numbers, powerball = [3,4,5,6,7], [8]
        user_numbers, user_powerball = [7,4,11,20,1], [1]

        correct_numbers, correct_powerball = number_check.number_check(numbers, powerball, user_numbers, user_powerball)

        self.assertEqual(correct_numbers, 2)
        self.assertEqual(correct_powerball, False)

    def test_number_check_powerball(self):
        '''Testing the number check function
        where powerball is guessed correctly
        '''

        numbers, powerball = [3,4,5,6,7], [8]
        user_numbers, user_powerball = [7,4,11,20,1], [8]

        correct_numbers, correct_powerball = number_check.number_check(numbers, powerball, user_numbers, user_powerball)

        self.assertEqual(correct_numbers, 2)
        self.assertEqual(correct_powerball, True)    