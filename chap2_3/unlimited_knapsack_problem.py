import pprint

N = int(input())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
LIMIT_WEIGHT = int(input())

dp = [[0 for _ in range(LIMIT_WEIGHT+1)] for _ in range(N+1)]
def solve():
    # i: 品物の番号
    for i in range(N):
        for j in range(LIMIT_WEIGHT+1):
            if j < W[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-W[i]] + V[i])
            pprint.pprint(dp)

    print(dp[N][LIMIT_WEIGHT])

if __name__ == '__main__':
    solve()