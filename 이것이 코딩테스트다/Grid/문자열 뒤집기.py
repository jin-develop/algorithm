S = input()

# 0001100  ->  1

# 101 -> 1

num_0 = 0
num_1 = 0

array = []

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        array.append(i+1)


arr1 = []


if len(array) % 2 != 0:
    print(int(len(array)//2)+ 1)
else:
    print(int(len(array) /2))

