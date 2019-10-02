N = int(input())
A = list(map(int, input().split()))
M = list(map(int, input().split()))
K = int(input())
dp = [-1 for _ in range(K+1)]

def solve():
    dp[0] = 0
    for i in range(N):
        for j in range(K+1):
            if dp[j] >= 0:
                dp[j] = M[i]
            elif j < A[i] or dp[j-A[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j-A[i]] - 1
    
    if dp[K] >= 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()