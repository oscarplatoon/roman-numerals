const romanNum = {
  "I"     : 1,
  "IV"    : 4,
  "V"     : 5,
  "IX"    : 9,
  "X"     : 10,
  "XIV"   : 14,
  "XLIV"  : 44,
  "L"     : 50,
  "C"     : 100,
  "D"     : 500,
  "CMXLIV": 944,
  "M"     : 1000
};
// Locate key by value
const getKey = (obj,val) => Object.keys(obj).find(key => obj[key] === val);

exports.toRoman = function(num) {
  let roman_str = '';
  while (num >= 1000) {
    roman_str = roman_str.concat(getKey(romanNum, 1000))
    num -= 1000
  }
  if (num === 944) {
    roman_str = roman_str.concat(getKey(romanNum, 944))
    num -= 944
  }
  while (num >= 500) {
    roman_str = roman_str.concat(getKey(romanNum, 500))
    num -= 500
  }
  while (num >= 100) {
    roman_str = roman_str.concat(getKey(romanNum, 100))
    num -= 100
  }
  while (num >= 50) {
    roman_str = roman_str.concat(getKey(romanNum, 50))
    num -= 50
  }
  if (num === 44) {
    roman_str = roman_str.concat(getKey(romanNum, 44))
    num -= 44
  }
  if (num === 14) {
    roman_str = roman_str.concat(getKey(romanNum, 14))
    num -= 14
  }
  while (num >= 10) {
    roman_str = roman_str.concat(getKey(romanNum, 10))
    num -= 10
  }
  if (num === 9) {
    roman_str = roman_str.concat(getKey(romanNum, 9))
    num -= 9
  }
  while (num >= 5) {
    roman_str = roman_str.concat(getKey(romanNum, 5))
    num -= 5
  }
  if (num === 4) {
    roman_str = roman_str.concat(getKey(romanNum, 4))
    num -= 4
  }
  while (num >= 1) {
    roman_str = roman_str.concat(getKey(romanNum, 1))
    num -= 1
  }

  console.log(roman_str)
  return roman_str

};




