


function solution(lottos, win_nums) {
    var answer = [];
    var rank =[6,6,5,4,3,2,1]
    var Cnt = 0;
    var Zero = 0;
    for (let i=0; i<lottos.length; i++){
        if (win_nums.includes(lottos[i])){
            Cnt += 1;
        }
        if (lottos[i] ==0){
            Zero += 1;
        }
    }
    
    
    answer[0] = rank[Cnt + Zero]
    answer[1] = rank[Cnt]
    return answer;
}
