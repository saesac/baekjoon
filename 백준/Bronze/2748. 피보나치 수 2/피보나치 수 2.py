list=[0, 1]
n=int(input())
for i in range(2, n+1):
    list.append(list[i-1]+list[i-2])
print(list[n])