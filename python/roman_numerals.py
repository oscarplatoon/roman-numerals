

def to_roman(num):
    CONST_DEC_TO_ROMAN = [ [1000, "M"], [500, "D"], [100, "C"], [50, "L"], [10, "X"], [5, "V"], [1, "I"]]

    roman = ""

    for index in range(len(CONST_DEC_TO_ROMAN)):
        roman += (num // CONST_DEC_TO_ROMAN[index][0]) * CONST_DEC_TO_ROMAN[index][1]
        num -= num // CONST_DEC_TO_ROMAN[index][0] * CONST_DEC_TO_ROMAN[index][0]

    
    return roman

def to_roman_modern(num):
    CONST_DEC_TO_ROMAN = [ [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [4, "IV"], [5, "V"], [1, "I"]]

    roman = ""

    for index in range(len(CONST_DEC_TO_ROMAN)):
        roman += (num // CONST_DEC_TO_ROMAN[index][0]) * CONST_DEC_TO_ROMAN[index][1]
        num -= num // CONST_DEC_TO_ROMAN[index][0] * CONST_DEC_TO_ROMAN[index][0]
    
    return roman
