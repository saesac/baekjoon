N=int(input())
save=[]
for i in range(N):
    file=input()
    save.append(file)
    if i==0:
        continue
    else:
        for j in range(len(save[i])):
            if save[i][j]!=save[i-1][j]:
                save[i]=save[i][:j]+'?'+save[i][j+1:]
print(save[N-1])