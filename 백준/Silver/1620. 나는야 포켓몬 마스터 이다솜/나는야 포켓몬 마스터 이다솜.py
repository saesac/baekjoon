import sys
n, m = map(int, sys.stdin.readline().split())
poketmon = {}
for i in range(1, n+1):
    name = str(input())
    poketmon[i] = name
    poketmon[name] = i
for i in range(m):
    search = str(sys.stdin.readline()).rstrip()
    if search.isdigit():
        print(poketmon[int(search)])
    else:
        print(poketmon[search])