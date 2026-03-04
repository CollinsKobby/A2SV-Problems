n, m = map(int, input().split(" "))
arr_n = list(map(int, input().split(" ")))
arr_m = list(map(int, input().split(" ")))

left = 0
right = 0
arr = []
while left < n and right < m:
    if arr_n[left] < arr_m[right]:
        arr.append(arr_n[left])
        left += 1
    else:
        arr.append(arr_m[right])
        right += 1

while left < n:
    arr.append(arr_n[left])
    left += 1

while right < m:
    arr.append(arr_m[right])
    right += 1

print(*arr)