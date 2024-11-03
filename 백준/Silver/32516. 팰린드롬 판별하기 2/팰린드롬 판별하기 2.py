def min_queries_to_check_palindrome(n, t):
    queries = 0
    left, right = 0, n - 1
    
    while left < right:
        if t[left] == '?' and t[right] == '?':
            queries += 26
        elif t[left] == '?' or t[right] == '?':
            queries += 1
        elif t[left] != t[right]:
            return 0
        left += 1
        right -= 1
    
    return queries

n = int(input())
t = input().strip()
print(min_queries_to_check_palindrome(n, t))