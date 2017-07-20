from queue import Queue
n, p = map(int, input().split())
q = Queue()
for i in range(n):
    l = input().split()
    q.put([l[0], int(l[1])])

r = []
t = 0

while not q.empty():
    d = q.get()
    if d[1] > p:
        q.put([d[0], d[1] - p])
        t += p
    else:
        t += d[1]
        r.append([d[0], t])
for d in r:
    print(d[0] + " " + str(d[1]))
