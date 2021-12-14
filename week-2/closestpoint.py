import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list1 = []
        list2 = []
        
        for i in range(len(points)):
            list1.append([(points[i][0])**2 + (points[i][1])**2, points[i]])
        minimum = float("inf")
        list1.sort()
        for j in range(k):
            list2.append(list1[j][1])
        return list2
