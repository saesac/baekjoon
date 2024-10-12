N, D, P = map(int, input().split())
mob = list(map(int, input().split()))
T = 0
isOverkilled = False
for i in range(N):
    if isOverkilled:
        isOverkilled = False
    elif i > 0 and mob[i-1] < 0:
        mob[i] -= -mob[i-1] * P // 100
        if mob[i] <= 0:
            isOverkilled = True
            continue

    while mob[i] > 0:
        mob[i] -= D
        T += 1
print(T)