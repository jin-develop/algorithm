


def solution(s):
    if s[0] == ')' or s[-1] == '(' or s.count('(') != s.count(')') or len(s) % 2 != 0:
        return False
    
    # ())(())
    k = 0
    for i in s:
        if i =='(':
            k += 1
        elif i ==')':
            k -= 1
        if k < 0:
            return False
        
    return True