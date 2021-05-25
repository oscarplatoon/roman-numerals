

exports.toRoman = function(num) {
  numeralConversion = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
  var romanReturn = []
  var balance = num
  for (entry in numeralConversion) {
    while (balance >= numeralConversion[entry]) {   
       balance -= numeralConversion[entry]
       romanReturn.push(entry)
      }
    }  
  return romanReturn.join('')
}

