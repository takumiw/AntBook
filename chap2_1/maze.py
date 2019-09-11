from collections import deque

H = int(input())
W = int(input())
maze = [list(input()) for _ in range(H)]
INF = 100000000
# 各点までの最短距離の配列
# 全ての点をINFで初期化
d = [[INF for _ in range(W)] for _ in range(H)]  

# 移動4方向のベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    que = deque()
    # スタート地点とゴール地点を走査
    for i in range(H):
        for j in range(W):
            if maze[i][j] == 'S':
                sx, sy = i, j
            elif maze[i][j] == 'G':
                gx, gy = i, j

    # スタート地点をキューに入れ、その点の距離を0にする
    que.append((sx, sy))
    d[sx][sy] = 0

    # キューが空になるまでループ
    while que:
        # キューの先頭を取り出す
        p = que.popleft()
        # 取り出してきた状態がゴールなら探索をやめる
        if p[0] == gx & p[1] == gy:
            break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を(nx, ny)とする
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            
            # 移動が可能の判定と既に訪れたことがあるかの判定
            if 0 <= nx and nx < H and 0 <= ny and ny < W and maze[nx][ny] != '#' and d[nx][ny] == INF:
                # 移動できるならキューに入れ、その点の距離をpからの距離+1で確定する
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]

if __name__ == "__main__":
    res = bfs()
    print(res)