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
import math
def to_roman(num):

    dict_roman_num = {
        'M' : 1000,
        'CM': 900,
        'D' : 500,
        'CD': 400, 
        'C' : 100,
        'XC': 90,
        'L' : 50,
        'XL': 40,
        'X' : 10,
        'IX': 9,
        'V' : 5,
        'IV': 4,
        'I' : 1
    }
    
    roman_char_list = [] # target list for appended roman chars from dict
    roman_value_list = [] # target list for appended values from dict
    
    roman_str = ''
    
    for roman_char, roman_value in dict_roman_num.items(): # 
        roman_char_list.append(roman_char)
        roman_value_list.append(roman_value)        
        # Create iterable lists from dict items of key, values
    
    
    index = 0
    while num > 0:
        for x in range(math.floor(num /roman_value_list[index])): #Iterate through the range of number / index at value list
            roman_str += roman_char_list[index] # roman string adds I
            # print(roman_str, roman_char_list[index])
            num -= roman_value_list[index] # num param decrements to 0 and breaks out
            # print(roman_value_list[index])
        index += 1 # add 1 to index value to iterate through lists
       
    return roman_str


