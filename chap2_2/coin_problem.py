C1, C5, C10, C50, C100, C500, A = map(int, input().split())
# コインの最大枚数
C = [C500, C100, C50, C10, C5, C1]
# コインの金額
V = [500, 100, 50, 10, 5, 1]

def solve():
    global A
    ans = 0

    for c, v in zip(C, V):
        t = min(A // v, c)  # コインcを使う枚数
        A -= t * v
        ans += t
    print(ans)

if __name__ == "__main__":
    solve()