exports.toRoman = function(num) {
  
  let outputString = '';
  let inputNumber = num

  //lookup dictionary must be greatest to smallest due to logic below.
  romanToArabic = {
    'M' : 1000,
    'CM' : 900,
    'D' : 500,
    'CD' : 400,
    'C' : 100,
    'XC' : 90,
    'L' : 50,
    'XL' : 40,
    'X' : 10,
    'IX' : 9,
    'V' : 5,
    'IV' : 4,
    'I' : 1,
  };

  //Starting from first key in the dictionary, working down through the values
  //Append roman numerals to the outputString.
  for (i in romanToArabic) {
   while (inputNumber >= romanToArabic[i]) {
    outputString += i;
    inputNumber -= romanToArabic[i];
   }
  }
  return outputString;
}
