exports.toRoman = function(num) {
    let roman = ''
    let romanObj = {M:1000,
        CM:900,
        D:500,
        CD:400,
        C:100,
        XC:90,
        L:50,
        XL:40,
        X:10,
        IX:9,
        V:5,
        IV:4,
        I:1
    }
  for ( i in romanObj ) {
    while ( num >= romanObj[i] ) {
      roman += i;
      num -= romanObj[i];
    }
  }
  return roman;
};


console.log(this.toRoman(150))