def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number_list = (lambda: list(map(int, input_list())))

    L, R = input_number_list()
    m = float('inf')
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            m = min(m, (i * j) % 2019)
            if m == 0:
                print(0)
                exit()
    print(m)


if __name__ == '__main__':
    main()
