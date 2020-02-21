import unittest


def calculator(x,y,op):
    valid_ops = ['+', '-', '/', '*']
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        return 'unknown value'

    if op not in valid_ops:
        return 'unknown value'

    return eval('{} {} {}'.format(x, op, y))


class MyTests(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator(6, '$', '+'), 8)

    def test_subtraction(self):
        self.assertEqual(calculator(4, 3, '-'), 1)

    def test_multiplication(self):
        self.assertEqual(calculator(5, 5, '*'), 25)

    def test_division(self):
        self.assertEqual(calculator(5, 4, '/'), 1.25)

    def test_unkown_value(self):
        self.assertEqual(calculator(6, 2, '&'), "unknown value")


if __name__ == '__main__':
    unittest.main()