li=[i for i in range(0, 251)]
while True:
    try:
        n = int(input())
        li[0], li[1], li[2] = 1, 1, 3
        for i in range(3, n+1):
            li[i] = li[i-1] + li[i-2]*2
        print(li[n])
    except:
        break