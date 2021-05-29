def to_roman(num):
    # Check input for correctness
    if num is None:
        return None
    elif not isinstance(num, int):
        return None

    int_roman_list = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    result = ""
    for (arabic, roman) in int_roman_list:
        (factor, num) = divmod(num, arabic)
        result += roman * factor

    return result

print(to_roman(1))