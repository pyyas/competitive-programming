class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        list1 = []
        ans = []
        diff = 0
        for i in range(len(l)):
            list1 = nums[l[i]:r[i]+1]
            list1.sort()
            diff = abs(list1[0] - list1[1])
            for j in range((len(list1)-1)):
                if abs(list1[j] - list1[j+1]) != diff:
                    ans.append(False)
                    break 
                elif j == (len(list1)-2) and abs(list1[j] - list1[j+1]) == diff:
                    ans.append(True)
        return ans
