def pancakeSort(self, arr: List[int]) -> List[int]:
        m, i, output = len(arr), 0, []        
        while i < len(arr):
            #print(i)
            if arr[i]==m:
                #print(arr, m, i)
                arr[:i+1] = reversed(arr[:i+1])
                #print(arr, 'first flip')
                arr[:m] = reversed(arr[:m])
                output.append(i+1)
                output.append(m)
                m -= 1
                i = -1
                #print(arr, 'second flip')
            i+=1
        return output
