N = int(input())
S = list(input())
S_reverse = list(reversed(S))

def solve():
    t = []
    while S:
        if S < S_reverse:
            t.append(S.pop(0))
            S_reverse.pop()
        else:
            t.append(S.pop())
            S_reverse.pop(0)
    print(''.join(t))

if __name__ == '__main__':
    solve()