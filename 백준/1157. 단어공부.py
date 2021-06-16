array = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']


txt = input()
txt = txt.lower()
ll = []
for i in array:
    ll.append(txt.count(i))

max1 = max(ll)

if ll.count(max1) > 1:
    print("?")
else:
    print(array[ll.index(max1)].upper())