s = list(map(int,input()))

print(s)
s.sort()
answer = s[0]

for i in range(1,len(s)):
    if answer == 0:
        answer += s[i]
    else:
        answer *= s[i]

print(answer)