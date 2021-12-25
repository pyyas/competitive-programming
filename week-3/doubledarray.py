class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        changed.sort()
        ans = []
        for i in changed:
            if count[i]>0:
                count[i] -= 1
                if count[2*i] > 0:
                    count[2*i] -= 1
                    ans.append(i)
                else:
                    return []
        return ans
