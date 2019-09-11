N = int(input())
W = list(map(int, input().split()))
V = list(map(int, input().split()))
B = int(input())
dp = [[-1 for _ in range(B+1)] for _ in range(N+1)]

def rec(i: int, j: int):
    '''
    重さがj以下になるように、i=0から初めて、i+1番目に入れた/入れない場合を再帰的に試行する
    @return res: バッグの中の品物の価値の総和
    '''
    global dp
    if dp[i][j] >= 0:  # 既に調べていれば、その結果を再利用
        return dp[i][j]
    if i==N:  # 品物は残っていない
        res = 0
    elif  W[i] > j:  # 品物は重すぎて入らない
        res = rec(i+1, j)
    else:  # 入れる場合と入れない場合を両方試す
        res = max(rec(i+1, j), rec(i+1, j-W[i]) + V[i])
    
    dp[i][j] = res
    return res

def solve():
    print(rec(0, B))

if __name__ == "__main__":
    solve()