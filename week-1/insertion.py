n = int(input())
arr = list(map(int, input().split()))


   
num = arr[n-1]
i = n-2
while i>=0:
    if arr[i]>num:
        arr[i+1]=arr[i]
        print(*arr)
        i-=1
    elif arr[i] <= num:
        arr[i+1] = num
        print(*arr)
        i = -1

if arr[0] > num:
    arr[0] = num
    print(*arr)
