def countSwaps(arr):
    # Write your code here
    n=len(arr)
    x=0
    for i in range(0,n):
        for j in range(0,n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                x+=1
    print('Array is sorted in', x, 'swaps.')
    print('First Element:', arr[0])
    print('Last Element:', arr[n-1])
