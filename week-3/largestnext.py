class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new = []
        wanted = []
        for i in nums1:
            new.append(nums2.index(i))
        for j in new:
            if max(nums2[j:]) > nums2[j]:
                maximum = nums2[j]
                while j < len(nums2):
                    if nums2[j+1] > maximum:
                        wanted.append(nums2[j+1])
                        j = len(nums2)
                    else:
                        j += 1
            else:
                wanted.append(-1)
        return wanted
    