exports.toRoman = function(num) {

    let values = [1000,500,100,50,10,5,1]
    let letters = ['M','D','C','L','X','V','I'] 
    let placeholder = []
    let results = []
    let answer = ''


    let remainder = num;

    for (key in values){
      while (remainder - values[key] >= 0)  {
            if ((remainder - values[key]) >= 0) {
                results.push(letters[values.indexOf(values[key],0)])
                remainder -= values[key]
               
            }
        }
    }
    
    let count = 0;
    let hold = ''
    for (key in (results)) {
        if (count === 4) {
            answer += (results[key-1] + letters[(letters.indexOf(results[key-1])- 1)])
            count = 1
            hold = results[key]
            placeholder = [results[key]]
        } 
        else if (results[key] == hold) {
            placeholder.push(results[key])
            count++
        } 
        else {
            answer += placeholder.join('')
            placeholder = [results[key]]
            hold = results[key]
            count = 1
        }
    } 
    
    if (count == 4) {
        answer += (results[key-1] + letters[(letters.indexOf(results[key-1])- 1)])
    } else {
        answer += placeholder.join('')
    }
    return(answer)
};

