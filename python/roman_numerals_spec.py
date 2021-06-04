import unittest
from roman_numerals import to_roman

class RomanNumeralsTestCase(unittest.TestCase):

  
    # add tests to cover different edge cases
    def test_output(self):
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(3), 'III')
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(944), 'CMXLIV')
        self.assertEqual(to_roman(150), 'CL')
        self.assertEqual(to_roman(2400), 'MMCD')

    
        # Output correct roman numerals
        

    def test_str(self):
        self.assertNotEqual(to_roman(1), str)
    
        # output returns  a string type
        

    def test_returns_modern_numerals(self):
        self.assertNotEqual(to_roman(4), 'IIII')

    #    output not in lazy roman numerals

    # IV -> 4
    # IX -> 9
    # XIV -> 14
    # XLIV -> 44
    # CMXLIV -> 944

    # to_roman(4) # 'IV'
    # to_roman(944) # 'CMXLIV'
    # to_roman(150) # CL
if __name__ == '__main__':
    unittest.main()