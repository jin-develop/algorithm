

def solution(n):
    
    b = bin(n)
    b = b[2:]
    
    n1 = b.count('1')
    
    while True:
        n += 1
        c = bin(n)
        c = c[2:]
        m1 = c.count('1')
        
        if m1 == n1 :
            break
        else:
            continue
    
    return n