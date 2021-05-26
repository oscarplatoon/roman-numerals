var rn = require("./romanNumerals");

// lazy test cases
console.log(rn.toRoman(1) === 'I');
console.log(rn.toRoman(3) === 'III');
console.log(rn.toRoman(4) === 'IIII');
console.log(rn.toRoman(300) === 'CCC');
console.log(rn.toRoman(123) === 'CXXIII');
console.log(rn.toRoman(2400) === 'MMCCCC');
console.log(rn.toRoman(939) === 'DCCCCXXXVIIII');

// modern test cases
console.log(rn.toRomanModern(1) === 'I');
console.log(rn.toRomanModern(3) === 'III');
console.log(rn.toRomanModern(4) === 'IV');
console.log(rn.toRomanModern(300) === 'CCC');
console.log(rn.toRomanModern(123) === 'CXXIII');
console.log(rn.toRomanModern(2400) === 'MMCD');
console.log(rn.toRomanModern(939) === 'CMXXXIX');
console.log(rn.toRomanModern(594) === 'DXCIV');
