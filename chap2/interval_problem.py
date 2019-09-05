from operator import itemgetter

N = int(input())
STARTS = list(map(int, input().split()))
ENDS = list(map(int, input().split()))

# 仕事をソートするための配列
jobs = [(s, e) for s, e in zip(STARTS, ENDS)]
# 終了時間が早い順にソートする
jobs.sort(key=itemgetter(1))

ans = 0
t = 0  # 最後に選んだ仕事の終了時間
for start, end in jobs:
    if start >= t:
        ans += 1
        t = end
print(ans)