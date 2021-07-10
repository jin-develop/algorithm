function solution(record) {
    var answer = [];
    var id ={};
    for (var i of record){
        var j = i.split(" ")
        if ( j[0] == 'Enter'){
            id[j[1]] = j[2]
        } else if (j[0] == 'Change'){
            id[j[1]] = j[2]           
        }
    }
    var a =''
    for (var s of record){
        a = ''
        var k = s.split(" ")
        if ( k[0] == 'Enter'){
            a = id[k[1]] + '님이 들어왔습니다.'
            answer.push(a)
        } else if (k[0] == 'Leave'){
            a = id[k[1]] + '님이 나갔습니다.'
            answer.push(a)
        } 
        
    }
    return answer;
}