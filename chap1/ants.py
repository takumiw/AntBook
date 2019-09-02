L = int(input())
N = int(input())
X = list(map(int, input().split()))

max_time = max(L-X[0], X[-1])
min_time = max(max(X[:N//2]), L-min(X[N//2:]))
print('min = {}'.format(min_time))
print('max = {}'.format(max_time))