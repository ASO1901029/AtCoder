def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N = input_number()
    ans = (N // 500)*1000
    N %= 500
    ans += (N // 5)*5
    print(ans)
if __name__ == '__main__':
    main()
