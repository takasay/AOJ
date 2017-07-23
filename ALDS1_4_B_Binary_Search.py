n1 = input()
t1 = list(map(int, input().split()))
n2 = input()
t2 = list(map(int, input().split()))
r = 0

for n in t2:
    h, t = 0, len(t1)
    while t - h > 1:
        v = int((t - h) / 2) + h
        # print(n, t1[v], h, t, v)
        if n == t1[v]:
            r += 1
            break
        elif n > t1[v]:
            h = v
        else:
            t = v
print(r)
