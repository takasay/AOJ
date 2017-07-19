def shell_sort(a, n):
    g = []
    h = 1
    while True:
        if h > n:
            break
        g.insert(0, h)
        h = h * 3 + 1
    c = 0
    print(len(g))
    print(' '.join(map(str, g)))
    for i in range(len(g)):
        c = insertion_sort(a, n, g[i], c)
    print(c)


def insertion_sort(a, n, g, c):
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            c += 1
        a[j + g] = v
    return c

n = int(input())
a = [int(input()) for _ in range(n)]
shell_sort(a, n)
for n in a:
    print(n)
