class Solution: 
    def select(self, arr, i):
        # code here 
        min = arr[i]
        index = i
        
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                index = j
        return min, index
        
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            min, index = self.select(arr, i)
            print("r",min, index)
            curr= arr[i]
            arr[i] = min
            arr[index] = curr
            print(arr)
        return arr
