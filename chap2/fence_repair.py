from heapq import heapify, heappush, heappop

N = int(input())
L = list(map(int, input().split()))

def solve():
    heapify(L)
    cost = 0
    while len(L) > 1:
        m1 = heappop(L)
        m2 = heappop(L)
        cost += (m1 + m2)
        heappush(L, m1+m2)
    
    print(cost)

if __name__ == '__main__':
    solve()