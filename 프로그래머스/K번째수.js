


function solution(array, commands) {
    var answer = [];
    
    for (var i in commands) {
        
        var new_arr = array.slice(commands[i][0]-1,commands[i][1])
        new_arr.sort(function(a,b){return a-b})
        
        answer.push(new_arr[commands[i][2]-1])
    }
    return answer;
}