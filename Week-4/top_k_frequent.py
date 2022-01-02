class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        list1= count.most_common(k)
        ans= []
        for i in list1:
            ans.append(i[0])
        return ans
