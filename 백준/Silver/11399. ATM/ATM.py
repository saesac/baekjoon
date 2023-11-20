n = int(input())
gr = [0] * n
time = sorted(list(map(int, input().split())))
for i in range(n):
    gr[i] = sum(time[:i+1])
print(sum(gr))