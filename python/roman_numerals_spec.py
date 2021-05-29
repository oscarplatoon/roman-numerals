import unittest
from roman_numerals import to_roman

class TestRoman(unittest.TestCase):
    """
    When you call to_roman with a non int parameter you get back None
    """

    def test_returns_none(self):
        self.assertTrue(to_roman("Hi!") == None)

    """
    When you call to_roman you get back proper modern roman conversion:
    """

    def test_roman_function(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(3), 'III')
        self.assertEqual(to_roman(4),  'IV')
        self.assertEqual(to_roman(2499), 'MMCDXCIX')
        
if __name__ == '__main__':
    unittest.main()


# print(to_roman(1) == 'I')
# print(to_roman(3) == 'III')
# print(to_roman(4) == 'IV')
# # add tests to cover different edge cases
