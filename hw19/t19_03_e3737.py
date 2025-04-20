if __name__=="__main__":
    with open('input.txt') as f:
        n = int(f.readline())
        heap = [0] + list(map(lambda x: int(x), f.readline().split()))
        for i in range(1, n+1):
            if 2*i <= n:
                if heap[i] > heap[2*i]:
                    print('NO')
                    break
            if 2*i+1 <= n:
                if heap[i] > heap[2*i+1]:
                    print('NO')
                    break
        else:
            print('YES')