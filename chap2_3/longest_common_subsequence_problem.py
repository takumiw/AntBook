N, M = map(int, input().split())
S = input()
T = input()
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
def solve():
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    print(dp[N][M])

if __name__ == '__main__':
    solve()