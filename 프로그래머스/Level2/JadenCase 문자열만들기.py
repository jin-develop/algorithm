def solution(s):
    answer = ''
    s  = s.lower()
    a = s.split(" ")
    sum1 = ""
    for i in a:
        
        i = i.capitalize()
        if sum1 == "":
            sum1 = i
        else:
            sum1 = sum1 + " " + i
        
        
    return sum1


