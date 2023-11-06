import sys
m = int(sys.stdin.readline())
sum=0
xor=0
for i in range(0, m):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        sum += query[1]
        xor ^= query[1]
    elif query[0] == 2:
        sum -= query[1]
        xor ^= query[1]
    elif query[0] == 3:
        print(sum)
    elif query[0] == 4:
        print(xor)