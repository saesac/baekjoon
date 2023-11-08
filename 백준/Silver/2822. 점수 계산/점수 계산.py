pt = []
for i in range(0, 8):
    pt.append(int(input()))
spt = sorted(pt)[3:]
print(sum(spt))
for i in range(0, 8):
    if pt[i] in spt:
        print(i + 1, end=' ')