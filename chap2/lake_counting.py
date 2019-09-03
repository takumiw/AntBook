H, W = map(int, input().split())

field = [['.']+list(input())+['.'] for _ in range(H)]
field.insert(0, ['.' for _ in range(W+2)])
field.append(['.' for _ in range(W+2)])

def dfs(h, w):
    field[h][w] = '.'
    # 移動する8方向をループ
    for dh in [-1, 0, 1]:
        for dw in [-1, 0, 1]:
            nh, nw = h + dh, w + dw
            if field[nh][nw] == 'W':
                dfs(nh, nw)
    return

def solve():
    lake_count = 0
    for h in range(1, H+1):
        for w in range(1, W+1):
            if field[h][w] == 'W':
                dfs(h, w)
                lake_count += 1
    print(lake_count)

if __name__ == "__main__":
    solve()