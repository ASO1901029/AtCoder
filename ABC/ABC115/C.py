def main():
    from builtins import int, map, list, float, print, min
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N, K = input_number_list()
    h = [input_number() for _ in range(N)]
    h.sort()
    ans = float('inf')
    for i in range(N - K + 1):
        ans = min(ans, h[i + K - 1] - h[i])
    print(ans)


if __name__ == '__main__':
    main()
