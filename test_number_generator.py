import unittest
import number_generator

class TestNumberGenerator(unittest.TestCase):

    def test_number_generator(self):
        '''Testing the number generator function'''
        numbers, powerball = number_generator.number_generator()

        self.assertEqual(len(numbers), 5)
        self.assertEqual(len(powerball), 1)

        for number in numbers:
            returned = number in range(1,50)
            message = "Not true"
            self.assertTrue(returned, message)

        self.assertTrue((powerball in range(1,20), message))
        

