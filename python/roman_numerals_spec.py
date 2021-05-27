from roman_numerals import to_roman
print ('1 thru 10')
print ('==================================')
print(to_roman(1) == 'I')
print(to_roman(2) == 'II')
print(to_roman(3) == 'III')
print(to_roman(4) == 'IV')
print(to_roman(5) == 'V')
print(to_roman(6) == 'VI')
print(to_roman(7) == 'VII')
print(to_roman(8) == 'VIII')
print(to_roman(9) == 'IX')
print(to_roman(10) == 'X')
print ('==================================')

print('Additional tests')
print ('==================================')
print(to_roman(68) == 'LXVIII')
print(to_roman(150) == 'CL')
print(to_roman(944) == 'CMXLIV')
print ('==================================')


# add tests to cover different edge cases
# print(to_roman() == '')