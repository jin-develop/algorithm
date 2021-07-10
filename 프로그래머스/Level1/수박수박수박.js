function solution(n) {
    var answer = '수박';
    var a = parseInt(n/2)
    if (n%2 !== 0){
        return answer.repeat(a)+'수'
    } else{
        
        return answer.repeat(a)
    }
    return answer;
}