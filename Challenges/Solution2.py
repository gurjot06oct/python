import copy
k=int(input("Dimensions: "))
array2d = [list(map(int, input().split())) for _ in range(k)]
RotatedArray=[]
n = int(input("Rotation Index:"))
move = -1 if n<0 else (1 if n>0 else 0)
dir=1
if n > 0:
    dir=0
if n==0:
   print(array2d)
else:
    RotatedArray=[[(i,j) for j in range(k)] for i in range(k)]
    layers= k//2 if k%2==0 else (k-1)//2
    if k%2 != 0:
        RotatedArray[layers][layers]=array2d[layers][layers]
    for _ in range(abs(n)):
        for  li in range(layers): 
            RotatedArray[li][dir + li+move:dir + k-1-li+move] = array2d[li][dir + li:dir + k-1-li]
            for i in range(dir+li,dir+k-1-li):
                RotatedArray[i+move][k-1-li] = array2d[i][k-1-li]
            RotatedArray[k-1-li][dir + li:dir + k-1-li] = array2d[k-1-li][dir + li+move:dir + k-1-li+move]
            for i in range(dir+li,dir+k-1-li):
                RotatedArray[i][li] = array2d[i+move][li]
        array2d = copy.deepcopy(RotatedArray)

for i in RotatedArray:
    print(i)