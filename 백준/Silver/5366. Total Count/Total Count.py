li = []
check = []
while True:
    try:
        data = input()
        if data == "0":
            break
        else:
            li.append(data)
            if data not in check:
                check.append(data)
    except:
        break
for i in check:
    print(i+": "+str(li.count(i)))
print("Grand Total: "+str(len(li)))