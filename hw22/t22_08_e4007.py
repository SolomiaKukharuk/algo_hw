from collections import deque

def check(n, cur, b, parr, q):
    if n == b and parr.get(n) is None:
        parr[n] = cur
        q.append(n)
        return True
    elif n == b:
        return True
    elif parr.get(n) is None:
        parr[n] = cur
        q.append(n)
        return False
    elif parr.get(n) is not None:
        return False

def bfs(a, b):
    q = deque()
    q.append(a)

    parr = {}
    parr[a] = -1

    while q:
        cur = q.popleft()

        if cur // 1000 != 9:
            n = (cur // 1000 + 1) * 1000 + cur % 1000
            if check(n, cur, b, parr, q):
                break

        if cur % 10 != 1:
            n = cur - 1
            if check(n, cur, b, parr, q):
                break

        n = cur // 10 + (cur % 10) * 1000
        if check(n, cur, b, parr, q):
            break

        n = (cur % 1000) * 10 + (cur // 1000)
        if check(n, cur, b, parr, q):
            break

    if parr.get(b) is None:
        print(-1)
        return

    st = []
    st.append(b)
    cur = b
    while cur != a:
        cur = parr[cur]
        st.append(cur)

    while st:
        print(st[-1])
        st.pop()

if __name__=='__main__':
    with open('input.txt') as f:
        start = int(f.readline())
        finish = int(f.readline())
    bfs(start, finish)
