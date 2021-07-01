
s = input()

s = list(s)


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

new1 = []
for i in array:
    if i == "":
        continue
    elif i[0] == "<":
        new1.append(i)
    else:
        
        space_idx =   [i for i, ele in enumerate(i) if ele == " "]
        print(space_idx)
        print(i)
        i = i.replace(" ", "")
        i = list(i)
        print(i)
        i = i[::-1]
        
        if len(space_idx) != 0 :
            for z in space_idx:
                i.insert(z, " ")
                print('ok')
        print(i)
        l = "".join(i) 
        new1.append(l)
print("".join(new1))
