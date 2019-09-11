from collections import deque

H = int(input())
W = int(input())
maze = [[-1]+list(input())+[-1] for _ in range(H)]
maze.insert(0, [-1 for _ in range(W+2)])
maze.append([-1 for _ in range(W+2)])
max_turn = H*W
# 移動4方向のベクトル
dh_list = (1, 0, -1, 0)
dw_list = (0, 1, 0, -1)

# スタート地点 -> 0, 壁 -> -1, ゴール地点/道 -> max_turn
for h in range(1, H+1):
    for w in range(1, W+1):
        if maze[h][w] == 'S':
            start = (h, w)
            maze[h][w] = 0
        elif maze[h][w] == 'G':
            goal = (h, w)
            maze[h][w] = max_turn
        elif maze[h][w] == '#':
            maze[h][w] = -1
        else:
            maze[h][w] = max_turn

queue = deque()
queue.append(start)
while queue:
    h, w = queue.popleft()
    if (h, w) == goal:
        break
    current_turn = maze[h][w]
    for dh, dw in zip(dh_list, dw_list):
        nh, nw = h+dh, w+dw
        if maze[nh][nw] > current_turn + 1:
            maze[nh][nw] = current_turn + 1
            queue.append((nh, nw))

print(maze[goal[0]][goal[1]])