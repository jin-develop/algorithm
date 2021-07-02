T = int(input())
for _ in range(T):
    s = input()
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = s[i][::-1]
        
    print(" ".join(s))