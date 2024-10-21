from itertools import permutations
n, m = map(int, input().split())
li=list(permutations(sorted(list(map(int, input().split()))), m))
for j in range(len(li)):
    print(' '.join(map(str, li[j])))