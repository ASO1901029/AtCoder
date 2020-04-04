def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N, X = input_number_list()
    a,p = [1],[1]
    for i in range(N):
        a.append(a[i]*2+3) #厚さ
        p.append(p[i]*2+1) #パティの数
    def f(N,X):
        if N==0:
            return 0 if X<= 0 else 1
        elif X<=1 +a[N-1]:
            return f(N-1,X-1)
        else:
            return p[N-1] + 1 + f(N-1,X-2-a[N-1])

    print(f(N,X))

if __name__ == '__main__':
    main()
