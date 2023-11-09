import math
num=str(math.factorial(int(input())))
cnt=0
for i in range(len(num)-1,-1,-1):
    if num[i]!='0':
        print(cnt)
        break
    else:
        cnt+=1