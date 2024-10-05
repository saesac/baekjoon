dct=[]
cnt=0
N=int(input())
for i in range(N):
    a, b = map(int,input().split())
    dct.append([a, b])
dct.sort()
for i in range(N):
    if cnt < dct[i][0]:
        cnt += dct[i][0]-cnt + dct[i][1]
    else:
        cnt += dct[i][1]
print(cnt)