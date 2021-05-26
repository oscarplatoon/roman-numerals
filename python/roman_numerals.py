def to_roman(num):
    roman_num = ""
    nums = {
          "M": 1000,
          "CM": 900,
          "D": 500,
          "CD": 400,
          "C": 100,
          "XC": 90,
          "L": 50,
          "XL": 40,
          "X": 10,
          "IX": 9,
          "V": 5,
          "IV": 4,
          "I": 1
          }

    for romans in nums:
        while num >= nums[romans]:
            roman_num += romans
            num -= nums[romans]

    output = roman_num

    print(output)
    return output