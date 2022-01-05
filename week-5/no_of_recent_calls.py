class RecentCounter:

    def __init__(self):
        self.data = deque()
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.data.append(t)
        self.cnt += 1
        while self.data and self.data[0]<(t-3000):
            self.data.popleft()
            self.cnt -= 1
        return self.cnt
