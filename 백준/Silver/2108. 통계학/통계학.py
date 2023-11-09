import sys
from collections import Counter
n=int(sys.stdin.readline())
num_list = []
for i in range(0, n):
    num_list.append(int(sys.stdin.readline()))
print(round(sum(num_list)/n))
num_list.sort()
if n%2==0:
    print((num_list[int(n/2)-1]+num_list[int(n/2)])/2)
else:
    print(num_list[int(n/2)])
cnt = Counter(num_list)
dic = cnt.most_common()
max_fq = dic[0][1]
fq_num_list = []
for num in dic:
    if num[1] == max_fq:
        fq_num_list.append(num[0])
if len(fq_num_list) == 1:
    print(fq_num_list[0])
else:
    print(fq_num_list[1])
print(max(num_list)-min(num_list))