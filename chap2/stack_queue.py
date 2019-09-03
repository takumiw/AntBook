from collections import deque

def stack(d=deque()):
    d.append(1)
    print(d)
    d.append(2)
    print(d)
    d.append(3)
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)

def queue(d=deque()):
    d.append(1)
    print(d)
    d.append(2)
    print(d)
    d.append(3)
    print(d)
    d.popleft()
    print(d)
    d.popleft()
    print(d)
    d.popleft()
    print(d)