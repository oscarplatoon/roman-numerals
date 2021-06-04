import unittest
from roman_numerals import to_roman

class armstrong_test(unittest.TestCase):
    '''Test that the output is a list'''

    def test_returns_3(self):
        self.assertEqual(to_roman(3), 'III')
    def test_returns_4(self):
        self.assertEqual(to_roman(4), 'IV')
    def test_returns_43(self):
        self.assertEqual(to_roman(43), 'XLIII')
    def test_returns_70(self):
        self.assertEqual(to_roman(70), 'LXX')
    def test_returns_3724(self):
        self.assertEqual(to_roman(3724), 'MMMDCCXXIV')

if __name__ == '__main__':
    unittest.main()
# add tests to cover different edge cases
