var rn = require("./romanNumerals");

console.log(rn.toRoman(1) === 'I');
console.log(rn.toRoman(3) === 'III');
console.log(rn.toRoman(4) === 'IV');
console.log(rn.toRoman(9) === 'IX');
console.log(rn.toRoman(14) === 'XIV');
console.log(rn.toRoman(44) === 'XLIV');
console.log(rn.toRoman(944) === 'CMXLIV');
console.log(rn.toRoman(1000) === 'M');

console.log(rn.toRoman(2000) === 'MM'); 

