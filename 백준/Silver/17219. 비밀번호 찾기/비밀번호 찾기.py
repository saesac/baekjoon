N, M = map(int, input().split())
dict = {}
for _ in range(N):
    site, pw = map(str, input().split())
    dict[site] = pw
for i in range(M):
    print(dict[input()])