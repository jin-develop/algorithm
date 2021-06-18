array = ["c=","c-","dz=","d-","lj","nj","s=","z="]

txt = input()
cnt = 0
for i in array:
    cnt += txt.count(i)
    txt = txt.replace(i," ")

txt = txt.replace(" ","")
print(cnt + len(txt))
