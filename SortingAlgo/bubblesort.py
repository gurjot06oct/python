lis=[6,3,8,2,4,0]
def swap(lis2,i,j):
    t= lis2[i]
    lis2[i]=  lis2[j]
    lis2[j]=t
for  i in range(len(lis)):
    for j in range(len(lis)-1):
        if lis[j] > lis[j+1]:
            swap(lis,j,j+1)


print(lis)
        