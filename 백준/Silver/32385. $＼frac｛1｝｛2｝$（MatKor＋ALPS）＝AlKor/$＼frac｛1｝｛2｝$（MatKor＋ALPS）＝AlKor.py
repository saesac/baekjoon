N=int(input())
li=[]
if N%2==0:
    num = N+1
    for i in range(int(N/2)+1):
        li.append(num+i)
        li.append(num-i)
    li=list(set(li))
    li.remove(N+1)
    li.append(N+1)
    print(' '.join(map(str,li)))
elif N%2==1:
    num = N
    for i in range(int(N/2)+1):
        li.append(num+i)
        li.append(num-i)
    li[0] -= N
    li[len(li)-1] += N
    li.remove(N)
    li.append(N)
    print(' '.join(map(str,li)))