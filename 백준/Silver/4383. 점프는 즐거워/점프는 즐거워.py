while True:
    try:
        input_list = list(map(int, input().split()))
        n = input_list[0]
        input_list.pop(0)
        if n == 1:
            print("Jolly")
        else:
            diff_list = set()
            for i in range(n-1):
                diff = abs(input_list[i] - input_list[i+1])
                if diff >= 1 and diff < n:
                    diff_list.add(diff)
            if len(diff_list) == n-1:
                print("Jolly")
            else:
                print("Not jolly")
    except:
        break