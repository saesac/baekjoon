N, K = map(int, input().split())
cnt = 0
for i in list(reversed([int(input()) for i in range(N)])):
    if i <= K:
        cnt+=K//i
        K-=i*(K//i)
print(cnt)