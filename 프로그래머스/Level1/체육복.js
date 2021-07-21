const solution = (n, lost, reverse) => {
    let answer = n - lost.length;
    
    
    lost = lost.filter((lostStudent) => {
        let revIdx = reverse.findIndex(reverseStudent => reverseStudent === lostStudent);
        if(revIdx === -1) return lostStudent
        else {
            reverse.splice(revIdx,1);
            answer++;
        }
    });
    
    
    
    lost.forEach(lostStudent => {
        let revIdx = reverse.findIndex(reverseStudent => lostStudent-reverseStudent == 1 || lostStudent-reverseStudent == -1);
        if(revIdx !== -1) {
            reverse.splice(revIdx,1);
            answer++;
        }
    });
    
    return answer;
};

