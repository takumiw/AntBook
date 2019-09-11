N = int(input())
S = list(input())

def solve():
    # S[a], S[a+1], ..., S[b]が残っている文字列
    a = 0
    b = N-1
    while a <= b:
        # 左から見た場合と右から見た場合を比較
        left = False
        for i in range(b-a+1):
            if S[a+i] < S[b-i]:
                left = True
                break
            elif S[a+i] > S[b-i]:
                left = False
                break
        if left:
            print(S[a], end='')
            a += 1
        else:
            print(S[b], end='')
            b -= 1
    print()

if __name__ == '__main__':
    solve()