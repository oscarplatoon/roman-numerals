# 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
# 2. Create a OUTPUT string, set to ''
# 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
# 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
# 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
# 6. If EVENLY_DIVISIBLE_TIMES >= 1
  # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
  # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
# 7. Return OUTPUT

#python
# I : 1
# V : 5
# X -> 10
# L -> 50
# C -> 100
# D -> 500
# M -> 1000

import math


def to_roman(num):

    roman_str = ''

    dict_roman_num = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    #print(type(dict_roman_num[1])) # 1

    for key in dict_roman_num:
        include = dict_roman_num.get(key)
        roman_char = dict_roman_num.values()
        
        result = math.floor(num / include)
        
        print(key, include, roman_char, result)

        for val in range(result):
            val += 1
            roman_str = roman_str + roman_char(val)

        num = num % include

        if num == 0:
            break
        
        #print(include,roman_char)






