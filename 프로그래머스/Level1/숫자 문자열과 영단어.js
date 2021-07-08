

function solution(s) {
    var answer = '';
    var array = ['zero','one','two','three','four','five','six','seven','eight','nine'];
    var idx_arr = [0,1,2,3,4,5,6,7,8,9];
    var pattern_eng = /[a-zA-Z]/;
    var txt = '';
    for (var i =0; i<s.length; i++){
        if (pattern_eng.test(s[i])){
            txt = txt + s[i];
            if (array.includes(txt)){
                var idx = array.indexOf(txt)
                answer = answer + String(idx_arr[idx])
                txt = ''
                }
            } else {
                answer = answer + s[i];
            }
        
    }

    return parseInt(answer);
}