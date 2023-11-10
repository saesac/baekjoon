n, p_li = int(input()), []
for i in range(n):
    w, h = map(int, input().split())
    p_li.append((w, h))
for m in p_li:
    cnt = 1
    for n in p_li:
        if (m[0]!=n[0]) & (m[1]!=n[1]):  
            if (m[0]<n[0]) & (m[1]<n[1]):
                cnt += 1
    print(cnt)