N = int(input())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
LIMIT_WEIGHT = int(input())
import pprint

dp = [[sum(W)+1 for _ in range(N*max(V)+1)] for _ in range(N+1)]
dp[0][0] = 0

def solve():
    for i in range(N):
        for j in range(N*max(V)+1):
            if j < V[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = min(dp[i][j], dp[i][j-V[i]] + W[i])
    
    res = 0
    for i in range(N*max(V)+1):
        if dp[N][i] <= LIMIT_WEIGHT:
            res = i
    print(res)

if __name__ == '__main__':
    solve()