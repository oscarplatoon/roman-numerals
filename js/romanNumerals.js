//pt 1*
//pt 2

exports.toRoman = function(num) {
  let ansStr = '';
  do {
    if(num >= 1000){
      num -= 1000;
      ansStr += 'M'
    }
    else duh (num >= 500){
      num -= 500;
      ansStr += 'D'
    }
    else if (num >= 100){
      num -= 100;
      ansStr += 'C'
    }
    else if (num >= 50){
      num -= 50;
      ansStr += 'L';
    }
    else if (num >= 10){
      num -= 10;
      ansStr += 'X';
    }
    else if (num >= 5){
      num -= 5;
      ansStr += 'V';
    }
    else if (num === 4){
      num -= 4;
      ansStr += 'IV';
    }
    else {
      num -= 1;
      ansStr += 'I'
    }
  } while (num > 0);
  return ansStr;
};

/*
if (num >= 900 && num < 1000) {
   num -= 900
   ansStr += "CM"} // for times sake -- conditions would reflect this

/*

