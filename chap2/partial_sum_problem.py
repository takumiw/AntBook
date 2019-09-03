N = int(input())
A = list(map(int, input().split()))
K = int(input())

def dfs(i, sum):
    # n個決め終わったら、それまでの和がKと等しいかを返す
    if i == N:
        return sum == K
    # A[i]を足さない場合
    if dfs(i+1, sum):
        return True
    # A[i]を足す場合
    if dfs(i+1, sum+A[i]):
        return True
    # a[i]を使う使わないに拘らずKが作れないので、Falseを返す
    return False

if dfs(0, 0):
    print('Yes')
else:
    print('No')