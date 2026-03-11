n, t = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()

count, mins = 0, 0
for i in range(len(arr)):
    mins += arr[i]
    if mins <= t:
        count += 1

print(count)