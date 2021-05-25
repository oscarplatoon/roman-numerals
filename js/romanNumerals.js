exports.toRoman = function(num) {

//   # 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
// # 2. Create a OUTPUT string, set to ''
// # 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
// # 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
// # 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
// # 6. If EVENLY_DIVISIBLE_TIMES >= 1
//   # 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
//   # 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
// # 7. Return OUTPUT
  
  let outputString = '';
  let inputNumber = num
  romanToArabic = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
  }
//  for (let key in romanToArabic) {
   
//  }

 while (inputNumber>=1000) {
   outputString += "M"
   inputNumber -= 1000;
 }
 while (inputNumber >= 500) {
   outputString += "D";
   inputNumber -= 500;
 }
 while (inputNumber >= 100) {
  outputString += "C";
  inputNumber -= 100
 }
 while (inputNumber>=50) {
   outputString += "L";
   inputNumber -= 50;
 }
 while (inputNumber >= 10) {
   outputString += "X";
   inputNumber -= 10; 
 }
 while (inputNumber >= 5) {
   outputString += "V";
   inputNumber -= 5;
 }
 while (inputNumber >= 1) {
   outputString += "I";
   inputNumber -= 1
 }
 console.log(outputString)
 return outputString;
};
