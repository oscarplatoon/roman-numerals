// 1. Write a method TO_ROMAN, TO_ROMAN takes in INPUT_NUMBER (an arabic number)
// 2. Create a OUTPUT string, set to ''
// 3. Create a ROMAN_NUMERAL_TO_ARABIC_MAP that includes roman numerals as keys, arabic numbers as values
// 4. Iterate over ROMAN_NUMERAL_TO_ARABIC_MAP, keep track of ROMAN_NUMERAL and ARABIC_NUMBER
// 5. Set EVENLY_DIVISIBLE_TIMES = INPUT_NUMBER / ARABIC_NUMBER:
// 6. If EVENLY_DIVISIBLE_TIMES >= 1
  // 6a. Append ROMAN_NUMERAL to OUTPUT EVENLY_DIVISIBLE_TIMES
  // 6b. Subtract ARABIC_NUMBER from INPUT_NUMBER EVENLY_DIVISIBLE_TIMES
// 7. Return OUTPUT


// I -> 1
// V -> 5
// X -> 10
// L -> 50
// C -> 100
// D -> 500
// M -> 1000


const decimalToRoman = [
    { 1000:   "M"},
    { 500:    "D"},
    { 100:    "C"},
    { 50:     "L"},
    { 10:     "X"},
    { 5:      "V"},
    { 1:      "I"}
]

const decimalToRomanModern = [
    { 1000:   "M"},
    { 900:    "CM"},
    { 500:    "D"},
    { 400:    "CD"},
    { 100:    "C"},
    { 90:     "XC"},
    { 50:     "L"},
    { 40:     "XL"},
    { 10:     "X"},
    { 9:      "IX"},
    { 5:      "V"},
    { 4:      "IV"},
    { 1:      "I"}
]


exports.toRoman = function(num) {
    return convertToRoman(num, decimalToRoman)
};

exports.toRomanModern = function(num) {
    return convertToRoman(num, decimalToRomanModern)
}





function convertToRoman(num, conversionData) {
    let romanStr = ""

    for (let obj of conversionData) {
        let inc = Object.keys(obj)[0]
        let roman = obj[inc]

        let result = Math.floor(num / inc) 

        for (let i = 0; i < result; i++) {
            romanStr += roman
        }

        num = num % inc

        if (num === 0) {
            break
        }
    } 
    //console.log(romanStr)
    return romanStr 
}


//exports.toRoman(683)
