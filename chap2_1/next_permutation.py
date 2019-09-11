from itertools import permutations

MAX_N = 10
used = [False for _ in range(MAX_N)]
perm = [None for _ in range(MAX_N)]

# {0, 1, 2, 3, ..., n-1}の並び替えn!通りを生成する
def permutation1(pos: int, n: int):
    if pos == n:
        # permに対する操作
        return
    
    # permのpos番目を0~n-1のどれにするかのループ
    for i in range(n):
        if not used[i]:
            perm[pos] = i
            # iを使ったのでフラグをTrueにしておく
            used[i] = True
            permutation1(pos+1, n)
            # 戻ってきたらフラグを戻しておく
            used[i] = False
    
    return

# 重複があっても全ての順列を生成する(2^N)
N = [i for i in range(4)]
for i in permutations(N):
    print(i)
