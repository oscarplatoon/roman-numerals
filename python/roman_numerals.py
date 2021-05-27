# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
# 2. Create a OUTPUT string, set to ''
# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
# 6. If EVENLY_DIVISIBLE_TIMES >= 1
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
# 7. Return OUTPUT

# I -> 1
# V -> 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000

# IV -> 4
# IX -> 9
# XIV -> 14
# XLIV -> 44
# CMXLIV -> 944

roman_dict = {
    1000: 'M',
    944:  'CMXLIV',
    500:  'D',
    100:  'C',
    50:   'L',
    44:   'XLIV',
    14:   'XIV',
    10:   'X',
    9:    'IX',
    5:    'V',
    4:    'IV',
    1:    'I'
}

def to_roman(num):
    # write your code here!
    roman_str = ''
    while (num != 0):
        if (num >= 1000):
            num -= 1000
            roman_str += roman_dict[1000]
        elif (num >= 944):
            num -= 944
            roman_str += roman_dict[944]
        elif (num >= 500):
            num -= 500
            roman_str += roman_dict[500]
        elif (num >= 100):
            num -= 100
            roman_str += roman_dict[100]
        elif (num >= 50):
            num -= 50
            roman_str += roman_dict[50]
        elif (num >= 44):
            num -= 44
            roman_str + roman_dict[44]
        elif (num >= 14):
            num -= 14
            roman_str += roman_dict[14]
        elif (num >= 10):
            num -= 10
            roman_str += roman_dict[10]
        elif (num >= 9):
            num -= 9
            roman_str += roman_dict[9]
        elif (num >= 5):
            num -= 5
            roman_str += roman_dict[5]
        elif (num >= 4):
            num -= 4
            roman_str += roman_dict[4]
        elif (num >= 1):
            num -= 1
            roman_str += roman_dict[1]
        else:
            return 0
    return roman_str

# print(to_roman(68))
