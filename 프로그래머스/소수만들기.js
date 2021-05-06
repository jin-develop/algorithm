

function solution(nums) {
    var answer = 0;
    var num_list = [];
    // 3개의 수를 더했을 때;
    for (var i =0; i<nums.length-2; i++){
        for (var j = i+1;  j < nums.length-1; j++){
            for (var k = j+1; k <nums.length; k++){
                num_list.push(nums[i]+nums[j]+nums[k])
            };
        };
    };
    
    for (var z=0; z<num_list.length; z++){
        var res = 0;
        var num1 = num_list[z]
        for (var kk=2; kk<parseInt(num1/2); kk++){
            if (num1%kk ==0)
                res++;
                
        };
        if (res == 0)
            answer++;
    };
    
    return answer
}