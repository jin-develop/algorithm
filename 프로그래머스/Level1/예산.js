


function solution(d, budget) {
    var answer = 0;
    d.sort(function(a,b){return a-b});
    var sum = 0;
    var Cnt = 0;
    for (let i =0; i<d.length; i++){
        Cnt++
        sum += d[i]
        if (sum > budget){
            Cnt--
            break;
        }
    }
    
    return Cnt;
}