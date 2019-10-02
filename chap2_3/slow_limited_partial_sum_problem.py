N = int(input())
A = list(map(int, input().split()))
M = list(map(int, input().split()))
K = int(input())
dp = [[False for _ in range(K+1)] for _ in range(N+1)]

def solve():
    dp[0][0] = True
    for i in range(N):
        for j in range(K+1):
            k = 0
            while k <= M[i] and k*A[i] <= j:
                dp[i+1][j] |= dp[i][j-k*A[i]]
                k += 1
    
    if dp[N][K]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    solve()