def toRoman (num):
  answer = ""
  map = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90,'L':50, 'XV':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

  # Checking for invalid number
  if num < 1 or num > 1000:
    return "Invalid"
   
  else:
    for key in map:
      # Getting index of num and assigning to a variable
      a = num // map[key]
      # Checking our new variable location in map
     
      if a==1:
      # Updates the answer with the correct index location
        answer += key

      # Stops infinite
      num = num % map[key]
    
  
  return answer


print(toRoman(999))