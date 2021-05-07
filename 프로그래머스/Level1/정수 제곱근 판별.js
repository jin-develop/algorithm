


function solution(n) {
    var answer = 0;
    var a = Math.sqrt(n)
    
    if (a % 1 == 0){
        return Math.pow(a+1,2)
    }else{
        return -1
    }
    
}