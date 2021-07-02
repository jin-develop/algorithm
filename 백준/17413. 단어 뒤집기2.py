


s = list(input())


array = []
tt = ""
rhkf = ""
for i in s:
    if i == '<':
        array.append(tt)
        tt =""
        rhkf += i
        continue
    elif i == ">":
        rhkf += i
        array.append(rhkf)
        rhkf = ""
        continue
    if len(rhkf) > 0:
        rhkf += i
    else:
        tt += i
array.append(tt)
print(array)
new1 = []
for i in array:
    if i == "":
        continue
    elif i[0] == "<":
        new1.append(i)
    else:
        a = i.split(" ")
        for zz in range(len(a)):
            a[zz] = a[zz][::-1]
        
        l = " ".join(a) 
        new1.append(l)

print(new1)
print("".join(new1))
