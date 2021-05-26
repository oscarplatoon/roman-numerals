def to_roman(num):  #modern
    numeral_return = ''
    value_array = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numeral_array = ['M','CM','D','CD','C','XC','L','XL','X','IX','V', 'IV','I']
    for int in value_array:
        while num >= int:
            num -= int
            numeral_return += numeral_array[(value_array.index(int))]
    return numeral_return

# def to_roman(num):  #lazy
#     numeral_return = ''
#     value_array = [1000, 500, 100, 50, 10, 5, 1]
#     numeral_array = ['M','D','C','L','X','V','I']
#     for int in value_array:
#         while num >= int:
#             num -= int
#             numeral_return += numeral_array[(value_array.index(int))]
#     return numeral_return

