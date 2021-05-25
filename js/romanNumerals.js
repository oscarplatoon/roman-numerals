function toRoman(num) {
  let answer = ''
  let arabic = num
  numeralsDecreasing = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
      }
  
  for (let i in numeralsDecreasing) {
    while (arabic >= numeralsDecreasing[i]) {
      answer += i;
      arabic -= numeralsDecreasing[i]
    }
  } 
  console.log(answer)
  return answer
  }
  
  toRoman();

