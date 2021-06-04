def to_roman(num):

    roman_dict = {

    'M': 1000,
    'CM' : 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
        
    } 
    
    roman_num = ''
    div = num / roman_dict['L']
    for i, r_num in enumerate(roman_dict):
        while (num>=roman_dict[r_num]):
            roman_num+= r_num
            num-= roman_dict[r_num]
    print(roman_num)
    return roman_num

to_roman(60)
        
        
        
        
    
