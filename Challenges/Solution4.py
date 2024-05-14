n= int(input())
a, b, c = 0, 1, 0

lis = [i if i < 2 else (c:=a+b) and (a:=b ) and (b:=c) for i in range(n)]
print(lis)