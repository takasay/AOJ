a = list(input().split())

s1 = s2 = []

for s in a:
    if s.isdigit():
        s1.append(s)
    else:
        if s1:
            p = int(s1.pop())
            if s == "+":
                s2.append(int(s1.pop()) + p)
            elif s == "-":
                s2.append(int(s1.pop()) - p)
            elif s == "*":
                s2.append(int(s1.pop()) * p)
        else:
            p = int(s2.pop())
            if s == "+":
                s2.append(int(s2.pop()) + p)
            elif s == "-":
                s2.append(int(s2.pop()) - p)
            elif s == "*":
                s2.append(int(s2.pop()) * p)
print(s2.pop())
