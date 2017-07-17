def sort_by_bubble(a, n):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if a[j][1] < a[j - 1][1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def sort_by_selection(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j][1] < a[minj][1]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
    return a


def is_array_stable(a1, a2):
    for i in range(len(a1)):
        for j in range(len(a2)):
            if a1[i][1] == a2[j][1]:
                if a1[i][0] != a2[j][0]:
                    return False
                else:
                    del a2[j]
                    break
    return True

n = int(input())
a = input().split()
ba = sort_by_bubble(a[:], n)
print(' '.join(ba))
bs = 'Stable' if is_array_stable(a, ba) else 'Not Stable'
print(bs)
sa = sort_by_selection(a[:], n)
print(' '.join(sa))
ss = 'Stable' if is_array_stable(a, sa) else 'Not stable'
print(ss)
