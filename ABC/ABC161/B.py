def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N, M = input_number_list()
    A = input_number_list()
    total = sum(A)
    cnt = 0
    for a in A:
        if a >= total / (4 * M):
            cnt += 1
    print('YNeos'[cnt < M::2])

if __name__ == '__main__':
    main()
