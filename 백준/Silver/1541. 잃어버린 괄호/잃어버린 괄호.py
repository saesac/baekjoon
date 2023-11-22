ex = input().split('-')
minus = []

for i in ex:
    cnt = 0
    temp_list = i.split('+')
    for j in temp_list:
        cnt += int(j)
    minus.append(cnt)

print(minus[0] - sum(minus[1:]))