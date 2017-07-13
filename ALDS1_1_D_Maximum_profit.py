import sys

n = int(input())
r = [int(input()) for _ in range(n)]

max_diff = -sys.maxsize
min_val = r[0]

for i in range(1, n):
    diff = r[i] - min_val
    if diff > max_diff:
        max_diff = diff
    if r[i] < min_val:
        min_val = r[i]

print(max_diff)
