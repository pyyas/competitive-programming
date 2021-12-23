import math

n, m, a = list(map(int, input().split()))
horizontal = math.ceil(n/a)
vertical = math.ceil(m/a)
print(horizontal*vertical)