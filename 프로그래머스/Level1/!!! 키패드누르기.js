function solution(numbers, hand) {
    var answer = '';
    var left_num = '147';
    var right_num = '369';
    var rand = '2580';
    var left = 3;
    var right = 3;
    var center = 0;
    
    for (var i =0; i<numbers.length; i++){
        
        if (left_num.includes(numbers[i])){
            answer = answer + 'L'
            left = left_num.indexOf(numbers[i])
        } else if (right_num.includes(numbers[i])){
            answer = answer + 'R'
            right = right_num.indexOf(numbers[i])
        } else {
            
            center = rand.indexOf(numbers[i])
            if (Math.abs(left - center) > Math.abs(right - center)) {
                answer = answer + 'R'
                right = rand.indexOf(numbers[i])
            } else if (Math.abs(left - center) < Math.abs(right - center)) {
                answer = answer + 'L'
                left = rand.indexOf(numbers[i])
            } else {
                if (hand =='left'){
                    answer = answer + 'L'
                    left = rand.indexOf(numbers[i])
                }else{
                    answer = answer + 'R'
                    right = rand.indexOf(numbers[i])
                }
            }
            
        }
    console.log(numbers[i] ,left, center, right)    
    }
    
    return answer;
}