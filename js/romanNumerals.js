exports.toRoman = function(num) {
  let ansStr = '';
  do {
    if(num >= 1000){
      num -= 1000;
      ansStr += 'M'
    }
    else if (num >= 500){
      num -= 500;
      ansStr += 'D'
    }
    else if (num >= 100){
      num -= 100;
      ansStr += 'C'
    }
    else if (num >= 50){
      num -= 50;
      ansStr += 'L'
    }
    else if (num >= 10){
      num -= 10;
      ansStr += 'X'
    }
    else if (num >= 5){
      num -= 5;
      ansStr += 'V'
    }
    else {
      num -= 1;
      ansStr += 'I'
    }
  } while (num > 0);
  console.log(ansStr)
};


