// exports.toRoman = function(num) {

// };

const toRoman = (num) => {
  let answer = "";
  
  const map = {
    M:1000,CM:900, D:500,CD:400, C:100, XC:90,L:50, XV:40, X:10, IX:9, V:5, IV:4, I:1
  }
  let a;
  // Checking for invalid number
  if (num < 1 || num > 3000) {
    return "Invalid";
  // 
  } else {
    for (let key in map) {
      // Getting index of num and assigning to a variable
      a = Math.floor(num / map[key]);
      // Checking our new variable location in map
      if(a >= 0) {
      // Filters the zeros out
        for(let i = 0; i < a; i++){
      // Updates the answer with the correct index location
          answer += key;
        }
      }
      // Stops infinite
      num = num % map[key];
    }
  }
  return answer;
}

console.log(toRoman(100));
