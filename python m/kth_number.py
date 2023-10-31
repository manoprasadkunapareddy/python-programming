def count_less_equal(x, m, n):
    count = 0
    for i in range(1, m+1):
        count += min(x // i, n)
    return count

def find_kth_element(m, n, k):
    left, right = 1, m*n
    
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid, m, n) < k:
            left = mid + 1
        else:
            right = mid
    
    return left

M = 3
N = 3
K = 5

result = find_kth_element(M, N, K)
print(f"The {K}th smallest element is: {result}")
