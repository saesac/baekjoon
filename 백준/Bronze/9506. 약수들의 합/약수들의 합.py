while True:
    n=int(input())
    if n==-1:
        break
    list=[]
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            list.append(i)
            if i!=n//i:
                list.append(n//i)
    list.sort()
    list.insert(0, 1)
    if sum(list)==n:
        print(n, " = ", " + ".join(map(str, list)), sep="")
    else:
        print(n, "is NOT perfect.")