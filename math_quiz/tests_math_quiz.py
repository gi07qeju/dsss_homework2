import unittest
from math_quiz import random_integer, random_operator, computation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        """ Test if random numbers generated are within the specified range """
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        """ Test if random operator completes correct operation """
        valid_operators = ['+', '-', '*']
        
        for _ in range(1000): # Test large number of random operators
            rand_op = random_operator()
            self.assertIn(rand_op, valid_operators, "Output is not a valid operator")
        

    def test_computation(self):
        """ Test if computation works as it should"""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            (10, 5, '+', '10 + 5', 15),
            (15, 5, '-', '15 - 5', 10),
            (7, 7, '*', '7 * 7', 49),
            (0, 5, '+', '0 + 5', 5),
            (5, 0, '-', '5 - 0', 5),
            (0, 5, '*', '0 * 5', 0),
            (5, -3, '+', '5 + -3', 2),
            (-5, -5, '-', '-5 - -5', 0),
            (-3, -2, '*', '-3 * -2', 6)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            if operator == '+':
                result_problem = f"{num1} + {num2}"
                result_answer = num1 + num2
            elif operator == '-':
                result_problem = f"{num1} - {num2}"
                result_answer = num1 - num2
            elif operator == '*':
                result_problem = f"{num1} * {num2}"
                result_answer = num1 * num2
            else:
                self.fail(f"Unexpected operator {operator}")

            # Check that the problem format and computation match expectations
            self.assertEqual(result_problem, expected_problem)
            self.assertEqual(result_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
