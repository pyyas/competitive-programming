def countingSort(arr):
    # Write your code here
    newlist = [0] * 100
    j = 0
    while j < n:
        newlist[arr[j]] += 1
        j += 1
    return newlist
