def solution(n):
    answer = ''
    
    while n:
        n, b= divmod(n, 3)
        answer = '412'[b] + answer
        if not b:
            n -= 1
        
    
    
    return answer

# 3진법의 형태를 사용해서 해결하기!!!