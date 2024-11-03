N = int(input().strip())
jung_base = input().strip()
jung_key = input().strip()
ian_base = input().strip()
ian_measure = input().strip()

new_key = []

for i in range(N):
    if jung_base[i] == ian_base[i]:
        if jung_key[i] != ian_measure[i]:
            print("htg!")
            break
        else:
            new_key.append(jung_key[i])
else:
    print("".join(new_key))