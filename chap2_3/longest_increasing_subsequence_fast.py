from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
INF = 1e6
dp = [INF for _ in range(N)]

def solve():
    for a in A:
        i = bisect_left(dp, a)
        dp[i] = a
    print(bisect_left(dp, INF))

if __name__ == '__main__':
    solve()