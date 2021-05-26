from roman_numerals import to_roman
from roman_numerals import to_roman_modern

print(to_roman(1) == 'I')
print(to_roman(3) == 'III')
print(to_roman(4) == 'IIII')
print(to_roman(505) == "DV")
print(to_roman(739) == "DCCXXXVIIII")
# add tests to cover different edge cases

print(to_roman_modern(4) == 'IV')
print(to_roman_modern(739) == "DCCXXXIX")
print(to_roman_modern(944) == "CMXLIV")