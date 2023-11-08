pt = []
for i in range(0, 8):
    pt.append(int(input()))
print(sum(sorted(pt)[3:]))
for i in range(0, 8):
    if pt[i] in sorted(pt)[3:]:
        print(i + 1, end=' ')