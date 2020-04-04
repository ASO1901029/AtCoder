def main():
    from builtins import int, map, list, print, max
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N = input_number()
    p = [input_number() for i in range(N)]
    ans = sum(p) - max(p) // 2
    print(ans)


if __name__ == '__main__':
    main()
