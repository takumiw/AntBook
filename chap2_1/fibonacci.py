import sys
sys.setrecursionlimit(10**6)

def fib_slow(n):
    if n <= 1:
        return n
    else:
        return fib_slow(n-1) + fib_slow(n-2)

memo = [0 for _ in range(10**6)]
def fib_fast(n):
    if n <= 1:
        return n
    if memo[n]:
        return memo[n] 
    memo[n] = fib_fast(n-1) + fib_fast(n-2)
    return memo[n]

f = [0, 1]
def fib(n):
    if n <= 1:
        return f[n]
    for i in range(2, n+1):
        f.append(f[-2]+f[-1])
    return f[n]