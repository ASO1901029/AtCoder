def main():
    from builtins import int, map, list, print
    import sys
    sys.setrecursionlimit(10 ** 6)

    input = sys.stdin.readline
    input_list = (lambda: input().rstrip().split())
    input_number = (lambda: int(input()))
    input_number_list = (lambda: list(map(int, input_list())))

    N = input_number()
    cnt = [0]

    def check(s=""):
        if int(s) > N:
            return 0
        rt = 1 if all(s.count(c) > 0 for c in '753') else 0
        for c in '753':
            rt += check(s + c)
        return rt

    print(check("0"))


if __name__ == '__main__':
    main()
