def solution(record):
    a = []
    obj = {}
    for re in record:
        re = re.split(" ")
        idx = re[1]
        if re[0] == "Enter":
            obj[idx] = re[2]
        elif re[0] == "Change":
            obj[idx] = re[2]
                    
    for rj in record:
        answer = ""
        rj = rj.split(" ")
        idx = rj[1]
        if rj[0] == "Enter":
            answer = obj[idx]+"님이 들어왔습니다."
            a.append(answer)
        elif rj[0] == "Leave":
            answer = obj[idx]+"님이 나갔습니다."
            a.append(answer)
            
    return a