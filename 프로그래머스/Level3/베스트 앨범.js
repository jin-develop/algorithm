function solution(genres, plays) {
    var answer = [];
    let obj = {};
    for(let i = 0; i<genres.length; i++){
        obj[genres[i]] = 0;
    }
    for(let i = 0; i<genres.length; i++){
        obj[genres[i]] += plays[i];
    }
    var sortable = [];
    for (var oob in obj) {
        sortable.push([oob, obj[oob]]);
    }
    sortable.sort((a,b) => b[1] - a[1]);
    
    for (let bb of sortable) {
        var exe = [];
        for (let i = 0; i<genres.length; i++) {
            if (bb[0] === genres[i]){
                exe.push([plays[i], i]);
            }
        }
        exe.sort((a,b) => b[0] - a[0]);
        if (exe.length === 1) {
            answer.push(exe[0][1]);
        } else{
            answer.push(exe[0][1]);
            answer.push(exe[1][1]);
        }
        
    }
    return answer;
}



// 새로운 Hash를 찾아서 써야한다...
