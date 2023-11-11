t=int(input())
for i in range(0, t):
    l_li=[]
    s_li=[]
    n=int(input())
    for j in range(0, n):
        s, l = input().split()
        s_li.append(str(s))
        l_li.append(int(l))
    m = l_li.index(max(l_li))
    print(s_li[m])