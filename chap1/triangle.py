N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

def solve():
    for i in range(N-2):
        a, b, c = A[i:i+3]
        if a < b + c:
            print(a + b + c)
            return
    print(0)
    return

if __name__ == "__main__":
    solve()