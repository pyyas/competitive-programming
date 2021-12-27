class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr), 0, -1):
            ans.append(arr.index(i) + 1)
            arr[:arr.index(i) + 1] = reversed(arr[:arr.index(i)+1])
            ans.append(i)
            arr[:i] = reversed(arr[:i])
        return ans
