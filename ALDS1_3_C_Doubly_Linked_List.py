n = int(input())
l = []
for _ in range(n):
    i = input().split()
    if i[0] == "insert":
        l.insert(0, i[1])
    elif i[0] == "delete":
        try:
            l.remove(i[1])
        except ValueError:
            pass
    elif i[0] == "deleteFirst":
        del l[0]
    else:
        del l[len(l) - 1]
print(" ".join(l))
