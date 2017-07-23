n1 = input()
t1 = input().split()
n2 = input()
t2 = input().split()
r = 0

for n in t2:
    if n in t1:
        r += 1
print(r)
