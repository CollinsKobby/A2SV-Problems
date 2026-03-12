n, s = map(int, input().split(" "))
nums =list(map(int, input().split(" ")))

curr_sum = 0
l, r = 0, 0
count = 0

while r < n:
    curr_sum += nums[r]
    if curr_sum <= s:
        count = max(count, r-l+1)
        r += 1
    else:
        curr_sum -= nums[l]
        l += 1
        r += 1
print(count)


