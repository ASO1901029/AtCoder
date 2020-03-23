def main():
    from builtins import int, map, list, print, min
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    L, X, Y, S, D = input_number_list()
    if Y > X:
        time1 = (D - S) / (X + Y) if D > S else (L - S + D) / (X + Y)
        time2 = (L - D + S) / (Y - X) if D > S else (S - D) / (Y - X)
        ans = min(time1, time2)
    else:
        ans = (D - S) / (X + Y) if D > S else (L - S + D) / (X + Y)
    print(ans)


if __name__ == '__main__':
    main()
