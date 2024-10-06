from itertools import combinations
N = int(input())
li=list(map(int, input().split()))
cnt=0
for i in range(N):
    li[i] = 1/li[i]
for r in range(1, N + 1):
    for combo in combinations(li, r):
        if 0.99 <= sum(combo) <= 1.01:
            cnt += 1
print(cnt)