import sys
n, m = map(int, sys.stdin.readline().split())
pfs = list(map(int, sys.stdin.readline().split()))

for i in range(n-1):
    pfs[i+1] += pfs[i]
pfs = [0] + pfs

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(pfs[j]-pfs[i-1])