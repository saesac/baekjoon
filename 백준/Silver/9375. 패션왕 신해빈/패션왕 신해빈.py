t = int(input())

for i in range(t):
    n = int(input())
    clothes_dict = {}
    for j in range(n):
        wear = list(input().split())
        if wear[1] in clothes_dict:
            clothes_dict[wear[1]].append(wear[0])
        else:
            clothes_dict[wear[1]] = [wear[0]]

    cnt = 1

    for k in clothes_dict:
        cnt *= (len(clothes_dict[k])+1)
    print(cnt-1)