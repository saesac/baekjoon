import sys
n = int(sys.stdin.readline())
if n == 0:
    print(0)
    sys.exit()
difficulty = []
for i in range(0, n):
    difficulty.append(int(sys.stdin.readline()))
difficulty.sort()
trimmed_mean = int((len(difficulty)*0.15)+0.5)
difficulty = difficulty[trimmed_mean:len(difficulty)-trimmed_mean]
print(int(sum(difficulty)/len(difficulty)+0.5))