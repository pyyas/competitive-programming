class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        main = sorted(count.values(), reverse=True)
        max_num = main[0]
        i = 0
        no_of_max_num = 0
        while i<len(main) and main[i] == max_num:
            no_of_max_num += 1
            i += 1
        ans = ((max_num-1) * (n+1)) + no_of_max_num
        return max(len(tasks), ans)
