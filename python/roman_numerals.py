def to_roman(num):
    result = ''
    roman_list = [
        [1000, 'M'],
        [500, 'D'],
        [100, 'C'],
        [50, 'L'],
        [10, 'X'],
        [5, 'V'],
        [1, 'I']
    ]
    for index, value in enumerate(roman_list):
        while num >= roman_list[index][0]:
           result += roman_list[index][1]
           num -= value[0]
    return result
    

print(to_roman(4))