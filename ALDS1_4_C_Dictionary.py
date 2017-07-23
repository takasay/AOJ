n = int(input())
d = {}

for _ in range(n):
    o, s = input().split()
    if o == "insert":
        d[s] = True
    else:
        try:
            if d[s]:
                print("yes")
        except:
            print("no")
