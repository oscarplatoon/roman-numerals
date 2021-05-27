def to_roman(num):
	output = ""
	roman_to_arabic = {
		"M": 1000,
		"CMXLIV": 944,
		"D": 500,
		"C": 100,
		"L": 50,
		"XLIV": 44,
		"XIV": 14,
		"X": 10,
		"IX": 9,
		"V": 5,
		"IV": 4,
		"I": 1
	}
	
	for x in roman_to_arabic:
		while (num >= roman_to_arabic[x]):
			output += x
			num -= roman_to_arabic[x]
			
	return output
		
print(to_roman(1))
print(to_roman(3))
print(to_roman(4))