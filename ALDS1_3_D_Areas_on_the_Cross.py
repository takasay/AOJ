d = 0
t = 0
p = True
puddles = []
s = []

for c in input():
    if c == "\\":
        if d >= 0:
            
            d = 0
        d -= 1
        s.append(c)
    elif c == "/":
        d += 1
        s.append(c)
    else:
        s.append(c)
