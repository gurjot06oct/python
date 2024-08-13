n = int(input("Enter the value of n: "))
first, second, temp = 0, 1, 0


fibonacci_series = [i if i < 2 else (temp:=first+second) and (first:=second) and (second:=temp) for i in range(n+1)]

print(fibonacci_series)
