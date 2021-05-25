// exports.toRoman = function(num) {

// };

const toRoman = (num) => {
  
  var romanNumerals = {
    1 : "I",
    5 : "V",
    10 : "X",
    50 : "L",
    100 : "C",
    500 : "D",
    1000 : "M",
  }

  let count = 0;
  var array = [];

for (let i=num; i > 5; i--) {
    let countTwo = 0;
    count++;
    countTwo++;
    array.push(romanNumerals[countTwo])
    // console.log(array.toString());
    
  }

  let x = (num - count);
  array.unshift(romanNumerals[x]);
  
  let y = (array.join(''));
  console.log(y);

}

toRoman(15);
