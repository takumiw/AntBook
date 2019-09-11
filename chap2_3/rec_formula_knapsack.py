N = int(input())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
B = int(input())
dp = [[0 for _ in range(B+1)] for _ in range(N+1)]

def solve():
    for i in range(N-1, -1, -1):
        for j in range(B+1):
            if W[i] > j:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i+1][j-W[i]] + V[i])
    print(dp[0][B])

if __name__ == "__main__":
    solve()