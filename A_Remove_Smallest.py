import math

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort()

    possible = "YES"
    for i in range(1, n):
        if a[i] - a[i-1] > 1:
            possible = "NO"
            break
    
    print(possible)
