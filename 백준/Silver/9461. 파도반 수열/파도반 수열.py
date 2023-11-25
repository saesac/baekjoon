for i in range(int(input())):
    n = int(input())
    dp = [1] * 101
    dp[4], dp[5] = 2, 2
    for i in range(6, n + 1):
        dp[i] = sum(dp[i-5:i-2])
    print(dp[n])