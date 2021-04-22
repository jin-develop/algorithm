

def solution(n):
    answer = []
    if n == 1 or n == 2:
        return 1
    
    for i in range(1, n//2+1):
        ans = 0
        j = i
        while True:
            ans += j
            if ans > n:
                break
            elif ans == n:
                answer.append(i)
                break
                
            j += 1
            
    return len(answer) + 1