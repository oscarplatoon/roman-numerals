exports.toRoman = function(num) {
  let output = '';
  let romanNumerals = {
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

   for (property in romanNumerals) {
     while (num>=romanNumerals[property]) {
      output = output.concat(property);
      num -= romanNumerals[property];
     }
   }
  return output;
  }
  