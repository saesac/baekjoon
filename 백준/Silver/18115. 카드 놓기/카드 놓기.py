from collections import deque

N=int(input())
A=list(map(int, input().split()))
dq=deque([])
A.reverse()
for i in range(N):
    if A[i]==1:
        dq.appendleft(i+1)
    elif A[i]==2:
        a=dq.popleft()
        dq.appendleft(i+1)
        dq.appendleft(a)
    elif A[i]==3:
        dq.append(i+1)
for i in dq:
    print(i, end=" ")