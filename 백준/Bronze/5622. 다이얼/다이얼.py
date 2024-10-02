list=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s=input()
cnt=0
for i in range(len(s)):
    for j in list:
        if s[i] in j:
            cnt+=list.index(j)+3
print(cnt)