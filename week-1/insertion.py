n, k = list(map(int, input().split()))
time = 240 - k
arr = [5]
i = 0
while i < n:
    arr.append(arr[-1]+5)
    if time < arr[-1]:
        print(i)
        break
    i += 1
if i == n:
    print(n)
