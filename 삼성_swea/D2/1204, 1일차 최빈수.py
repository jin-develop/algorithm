array = [1,2,3,7,5,1,2,6,3,6,2,12,3,12,3,3,4]

set_array = set(array)

set_array = list(set_array)
new_array = []
new_dict = {}
for i in set_array:
    
    count_i = array.count(i)
    
    new_dict[i] = count_i

print(new_dict.items())

ka = sorted(new_dict.items(), key=lambda x: x[1])

print(ka)