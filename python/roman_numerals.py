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

    output = ""
    for x in roman_dict:
       #print (roman_dict[x])
        while (num>=roman_dict[x]):
            output = output + x
            num = num - roman_dict [x]

    return output
to_roman(60)
        
        
        
        
    
