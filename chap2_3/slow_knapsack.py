N = int(input())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
B = int(input())

def rec(i: int, j: int):
    '''
    重さがj以下になるように、i=0から初めて、i+1番目に入れた/入れない場合を再帰的に試行する
    @return res: バッグの中の品物の価値の総和
    '''
    if i==N:  # 品物は残っていない
        res = 0
    elif  W[i] > j:  # 品物は重すぎて入らない
        res = rec(i+1, j)
    else:  # 入れる場合と入れない場合を両方試す
        res = max(rec(i+1, j), rec(i+1, j-W[i]) + V[i])
    return res

def solve():
    print(rec(0, B))

if __name__ == "__main__":
    solve()